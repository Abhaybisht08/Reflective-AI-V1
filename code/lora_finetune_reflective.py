"""
lora_finetune_reflective.py

This script fine-tunes a base open-source LLM (e.g., Mistral, GPT-J) using the Reflective-AI dataset.
Applies LoRA (Low-Rank Adaptation) for efficient parameter tuning.
"""

from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from peft import get_peft_model, LoraConfig, TaskType
from datasets import load_dataset
import torch

# Load dataset
dataset = load_dataset("json", data_files={"train": "data/reflective_dataset.json"}, split="train")

# Load tokenizer and model
model_id = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype=torch.float16)

# Apply LoRA
lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)
model = get_peft_model(model, lora_config)

# Tokenize dataset
def tokenize(batch):
    inputs = batch["Prompt"]
    outputs = batch["Reflected Output"]
    return tokenizer(
        inputs + "\n###\n" + outputs,
        padding="max_length",
        truncation=True,
        max_length=512,
    )

tokenized_dataset = dataset.map(tokenize, batched=True)

# Training
training_args = TrainingArguments(
    output_dir="./checkpoints/reflective-lora",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=3,
    fp16=True,
    logging_steps=10,
    save_steps=100,
    save_total_limit=2,
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False),
)

trainer.train()
model.save_pretrained("./checkpoints/reflective-lora")
tokenizer.save_pretrained("./checkpoints/reflective-lora")
