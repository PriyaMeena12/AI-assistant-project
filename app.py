
# from flask import Flask,render_template,request
# from dotenv import load_dotenv
# import os
# from openai import OpenAI
# load_dotenv()
# #print("API KEY:", os.getenv("OPENAI_API_KEY"))

# client=OpenAI(api_key=os.getenv ("OPENAI_API_KEY" ))
# app=Flask(__name__)

# @app.route('/',methods=['GET', 'POST'])
# def home():
#     response = ""
#     if request.method == 'POST':
#         user_input = request.form["user_input"]
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#             {"role":"system","content":"You are a helpful assistant"},
#              {"role":"user","content":user_input}
#             ]
#         )
#         response=completion.choices[0].message.content

#     return render_template("index.html", response=response)
    
# if __name__=="__main__":
#     app.run(debug=True)
 
 ############### Final ---------------------------------------------
    

# from flask import Flask, render_template, request
# from dotenv import load_dotenv
# import os
# from openai import OpenAI, RateLimitError

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     response = ""
#     if request.method == 'POST':
#         user_input = request.form["user_input"]
#         try:
#             completion = client.chat.completions.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": user_input}
#                 ]
#             )
#             response = completion.choices[0].message.content
#         except RateLimitError:
#             response = "⚠️ You've exceeded your OpenAI API quota. Please check your plan or try again later."
#         except Exception as e:
#             response = f"❌ Error occurred: {str(e)}"

#     return render_template("index.html", response=response)

# if __name__ == "__main__":
#     app.run(debug=True)
    




### with summarize option


from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from openai import OpenAI, RateLimitError

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    user_input = ""
    selected_task = ""
    
    if request.method == 'POST':
        user_input = request.form["user_input"]
        selected_task = request.form["task"]

        if not user_input.strip():
            response = "⚠️ Please enter some text."
        else:
            try:
                # Task-based prompting
                if selected_task == "summarize":
                    prompt = f"Summarize the following text:\n{user_input}"
                elif selected_task == "creative":
                    prompt = f"Write a short story or poem about:\n{user_input}"
                else:
                    prompt = user_input  # Default Q&A

                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                response = completion.choices[0].message.content

            except RateLimitError:
                response = "⚠️ You've exceeded your OpenAI API quota. Please check your plan or try again later."
            except Exception as e:
                response = f"❌ Error occurred: {str(e)}"

    return render_template("index.html", response=response, user_input=user_input, selected_task=selected_task)

if __name__ == "__main__":
    app.run(debug=True)

