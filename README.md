# Chatbot with Integrated LLM and State Graph

This project implements a chatbot application powered by **LangGraph** and **Langchain Groq**, using **Gradio** to provide a user-friendly interface. The chatbot utilizes a state graph to efficiently manage the flow of conversation and responds to user inputs by invoking a large language model (LLM).

---

## Features

- **State Graph Management**: Uses LangGraph’s StateGraph to define and manage the flow of conversation.
- **LLM Integration**: Powered by Groq's large language model (`Gemma2-9b-It`).
- **Gradio Interface**: Offers an interactive web-based user interface with customizable styling.
- **Exit Functionality**: Gracefully exits the chat session when the user types "quit", "q", or "exit".

---

## Prerequisites

### Python Libraries
Ensure you have the required Python packages installed:

```bash
pip install langchain langgraph gradio langchain_groq
```

### API Keys
- **Groq API Key**: Required for interaction with the LLM.
- **LangSmith API Key** (optional): For advanced logging and debugging.

API keys must be securely stored and retrieved in your script, e.g., using Google Colab’s `userdata` or environment variables.

---

## How to Run the Application

### 1. Run the Script
Execute the script using Python:

```bash
python chatbot_with_gradio.py
```

### 2. Access the Gradio Interface
After running the script, Gradio will provide a link, such as:

```text
Running on local URL: http://127.0.0.1:7860
```

Open the link in your browser to start interacting with the chatbot.

---

## Usage Instructions

### Command-Line Chatbot (Without UI)
If running without the Gradio interface, you can interact via the terminal:

```bash
User: Hello
Assistant: Hi! How can I assist you today?

User: What is 2 + 2?
Assistant: The result is 4.

User: quit
Goodbye
```

### Gradio Chatbot Interface
1. Launch the Gradio interface.
2. Type your query into the text box and press "Send."
3. View the chatbot’s response in the chat window.
4. To exit, type "quit", "q", or "exit."

---

## Code Explanation

### Key Components

1. **LangGraph and StateGraph**:
   - `StateGraph` defines the chatbot’s workflow.
   - The chatbot node (`chatbot`) processes user inputs using the `ChatGroq` model.

2. **Chatbot Functionality**:
   - The `chatbot` function processes the user state and invokes the LLM to generate responses.

3. **Gradio Interface**:
   - A web-based UI created using Gradio’s `Blocks` API.
   - CSS customization allows for styling the chat window, buttons, and overall layout.

4. **Exit Command**:
   - Handles user inputs like "quit" or "exit" to terminate the chat session.

---

## Example Usage

### Input
```text
Hello
```

### Output
```text
Assistant: Hi! How can I assist you today?
```

---

## Customization

### Changing the Language Model
Update the `model_name` in the `ChatGroq` initialization to use a different LLM:

```python
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Your-Model-Name")
```

### Modifying the Gradio UI
The Gradio UI styling can be updated in the `css` block:

```css
.gradio-container {background-color: #2c2f33; color: white;}
.chatbot {background-color: #23272a; color: white;}
.input-container {background-color: #40444b;}
button {background-color: #7289da; color: white;}
button:hover {background-color: #5b6eae;}
```

### Exit Conditions
You can modify the exit conditions by editing the following lines:

```python
if user_input.lower() in ["quit", "q", "exit"]:
    print("Goodbye")
    break
```

---

## Troubleshooting

### Common Errors

#### 1. Invalid API Key
If you encounter an error like:

```text
Error: 401 - Invalid API Key
```

Ensure you have set a valid Groq API key in `userdata` or as an environment variable.

#### 2. AIMessage Object Not Subscriptable
If you see:

```text
TypeError: 'AIMessage' object is not subscriptable
```

Verify that the `state["messages"]` is correctly handled in the chatbot function. Ensure the LLM returns a `content` attribute.

---

## Credits
This project was built using:
- [LangGraph](https://github.com/langgraph)
- [Langchain Groq](https://github.com/langchain/langchain_groq)
- [Gradio](https://www.gradio.app/)

---

## License
This project is licensed under the MIT License. Feel free to modify and distribute it as needed.

