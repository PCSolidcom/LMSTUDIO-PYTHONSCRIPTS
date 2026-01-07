from lmstudio import sync_api, list_downloaded_models, get_default_client
from lmstudio import ModelQuery
import time
import lmstudio as lms

#MODEL_SPEC = "qwen/qwen3-4b-thinking-2507"
#model = lms.llm(MODEL_SPEC)
#PROMPT = "100 of the best money making idea generation prompts ever written. Based on the most number of people who have made the most money each or total. Focus on real jobs such as stump grinding, wood chipping, parking lot striping, parking lot sealing, pressure washing homes and businesses, etc.  As well as remote computer, information, data, and similar jobs that can be done either remotely or in person. List the income idea, as well as the low, median, and high potential income of each along with the approximately yearly income of each."

print("--------------------------------------------------------")

from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
print(current_time)
#print(datetime.now().strftime("%Y-%m-%d %H:%M"))

#model = lms.llm("qwen/qwen3-4b-thinking-2507")

start_time = None
total_tokens = 0

def on_first_token():
#    print()
#    print("""---------------------- ENTERED: def on_first_token():""")
    global start_time
    start_time = time.perf_counter()

def on_fragment(fragment):
    global total_tokens
    text = getattr(fragment, "text", None)
    if text is None:
        text = getattr(fragment, "delta", None) or getattr(fragment, "content", None)
    if text is None:
        text = str(fragment)
    print(text, end="", flush=True)

    tokens_in_frag = getattr(fragment, "token_count", None) or getattr(fragment, "tokens", None)
    if tokens_in_frag is None:
        tokens_in_frag = len(text.split())
    try:
        tokens_in_frag = int(tokens_in_frag)
    except Exception:
        tokens_in_frag = len(str(tokens_in_frag))
    total_tokens += tokens_in_frag

def on_message(message):
    print()
#    print("""---------------------- ENTERED: def on_message(message):""")
    #print("\n\n--- final ---\n", message.content)
    if start_time:
        elapsed = time.perf_counter() - start_time
        final_tps = total_tokens / elapsed if elapsed > 0 else float("inf")
        print()
        print(f"\nModel: {MODEL_SPEC}  | Final tokens: {total_tokens} | elapsed: {elapsed:.2f}s | tokens/sec: {final_tps:.2f}")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        print()
        print(current_time)


###### PROMPTS BEGIN #############




start_time = None
total_tokens = 0
MODEL_SPEC = "qwen/qwen3-4b-thinking-2507"
model = lms.llm(MODEL_SPEC)

chat = lms.Chat()
time_curr=datetime.now().strftime("%Y-%m-%d %H:%M")
count="Model Name: kimi-vl-a3b-instruct-i1, Model Number: 1, Question Number: 1, Model Size: 9.71"
prompt="""You are a genius financial expert, analyze the following scenario and offer advice for maximizing all areas and pillars of life, focusing on my accumulation phase of life, maximizing profits and increasing net worth to the maximum possible.")"""
print ("--------------------------------TIME: " + time_curr + " " + count + ", PROMPT:" + prompt)
print()
chat.add_user_message(prompt)

stream = model.respond_stream(
    chat,
    on_first_token=on_first_token,
    on_prediction_fragment=on_fragment,
    on_message=on_message
)
for _ in stream:
    pass

#COMPLETED PROMPT RESPONSE SOUND
import winsound
frequency = 100  # Hz
duration = 1000  # ms
winsound.Beep(frequency, duration) 


start_time = None
total_tokens = 0
MODEL_SPEC = "qwen/qwen3-4b-thinking-2507"
model = lms.llm(MODEL_SPEC)

chat = lms.Chat()
time_curr=datetime.now().strftime("%Y-%m-%d %H:%M")
count="Model Name: kimi-vl-a3b-instruct-i1, Model Number: 1, Question Number: 2, Model Size: 9.71"
prompt="""Generate at least 10 comprehensive and detailed prompts that will help maximize the use of my education, skills, knowledge and resources. <List education, skills, knowledge, and resources here>")"""
print ("--------------------------------TIME: " + time_curr + " " + count + ", PROMPT:" + prompt)
print()
chat.add_user_message(prompt)

stream = model.respond_stream(
    chat,
    on_first_token=on_first_token,
    on_prediction_fragment=on_fragment,
    on_message=on_message
)
for _ in stream:
    pass

#COMPLETED PROMPT RESPONSE SOUND
import winsound
frequency = 100  # Hz
duration = 1000  # ms
winsound.Beep(frequency, duration) 


###### PROMPTS END #############

print()
time_curr=datetime.now().strftime("%Y-%m-%d %H:%M")
print(time_curr)

#unload model
model = lms.llm()
model.unload()
print ("-------------------")
