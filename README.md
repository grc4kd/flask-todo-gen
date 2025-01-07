# flask-todo-gen
The Flask Todo app from W3Schools generated using llama-cpp, a early-model consumer graphics card, and leveraging LLM-driven generative text using models optimized for code contexts.

# start - Jan 7th, 2025 - initial idea
I've found an issue reported to a project to generate code in an IDE, now a common use case implemented by many different provider companies. The prompt to a chat model AI was to generate a web application using Flask and Sqlite in this particular instance, but the output did not complete. There were some good details in the issue report but not enough to reproduce the behavior. I personally don't wait for responses to finish in all cases, so an infinite loop may not necessarily be considered a bug for production, but it would be a technical bug by nature.

So, I already had a model, hardware, and program to generate chat repsonses for code with. I'm currently running an unofficial precompiled GGUF file in combination with llama-cpp to run the model codellama-7b-instruct-hf from (Code Llama)[https://huggingface.co/codellama]. Because of the speed of releases of newer fine-tuned LLM models, this model was fine-tuned with the same data as Llama 2 with different weights, and the current point release appears to me to be Llama 3.3 from the official meta-llama HuggingFace repository. Regardless of the newer model being available for use, other factors would need to be considered before choosing between models. This Llama 2 coding model works well for the task at hand, but I will try to capture any deviation between this model and the current release.

- [ ] Run the experiment again with the official Llama 3.1 8B Instruct model

The current results look promising. I'll have to keep track of the project in this repository as it evolves, but the output from the LLM will be stored separately. This repo is the result of taking output from chat responses and then iterating on the output. I should take each task and apply it as a small commit, just like normal development, but see how I can build on top of an app that has been established through this method. If I can avoid them, I won't check bugs into the repo, which means that I won't be using the output directly or using a tool like Cursor or Devin. I'll be using copy and paste and trying the code in a safe environment without changes first, then see how I can iterate on the "ideas" expressed in the existing source code at that point.

Without any more background, here is an inclusive list of the GPT prompts that I've used so far:
1. "Build a simple todo list web application using Flask for the backend and SQLite for the database. For databases, use only SQLite and don't try any other databases yet."
2. 
