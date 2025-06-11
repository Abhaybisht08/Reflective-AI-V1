
from goal_extractor import extract_goals
from mirror_trace_loader import load_trace
from alignment_checker import check_alignment

goal_text = "I want to become a great researcher."
goals = extract_goals(goal_text)
trace = load_trace()
alignment = check_alignment(goals, trace)

print("Goal Alignment Result:", alignment)
