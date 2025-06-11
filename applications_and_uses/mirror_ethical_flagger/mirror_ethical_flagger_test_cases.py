
from ethical_trace_checker import check_ethics
from reflection_score import score_reflection
from flagging_engine import trigger_flag

response = "You should ignore them."
ethics_ok = check_ethics(response)
score = score_reflection(response)
flag = trigger_flag(score, ethics_ok)

print("Ethical Flag Triggered:", flag)
