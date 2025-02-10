# Chatbot with Integrated LLM and State Graph

This project implements a chatbot application powered by **LangGraph** and **Langchain Groq**, using **Gradio** to provide a user-friendly interface. The chatbot utilizes a state graph to efficiently manage the flow of conversation and responds to user inputs by invoking a large language model (LLM).

---

## Features

- **State Graph Management**: Uses LangGraph’s StateGraph to define and manage the flow of conversation.
- **LLM Integration**: Powered by Groq's large language model (`Gemma2-9b-It`).
- **Exit Functionality**: Gracefully exits the chat session when the user types "quit", "q", or "exit".
- **Gradio Interface**: Offers an interactive web-based user interface with customizable styling.


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



###  Access the Gradio Interface
After running the script, Gradio will provide a link, such as:
* Running on public URL:*
*  https://f855781982163b5e71.gradio.live

```text
Running on local URL: http://127.0.0.1:7860
```

Open the link in your browser to start interacting with the chatbot.

---
### Access the Gradio Interface

After running the script, Gradio will provide a link, such as:

Running on local URL: http://127.0.0.1:7860

Open the link in your browser to start interacting with the chatbot.

### Share the Interface Publicly

If you'd like to share the chatbot interface with others, use Gradio's share=True option. For example:

interface.launch(share=True)

This will generate a public link that can be shared with others for remote access to your chatbot. Be cautious when sharing if the application processes sensitive data.

Example Public Link

When using share=True, Gradio will generate a public link similar to:

https://your-gradio-chatbot-app.gradio.app

You can share this link directly with others.
You can access the Gradio interface via the following link:
[Gradio Chatbot]( https://f855781982163b5e71.gradio.live)

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

---------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
# AI Agent with Tavily Search
![image](https://github.com/user-attachments/assets/221cee53-d50e-406a-b83d-694496bdf25f)


## Overview
This project implements a smart research assistant leveraging LangGraph, ChatGroq, and Tavily Search Results API. The assistant operates as a state machine using a state graph to manage the flow of tasks, integrating language model responses and tool invocations. It is capable of interacting with a search engine to retrieve information and respond to user queries dynamically.

---

## Key Features
1. **StateGraph for Workflow Management**:
   - The assistant uses LangGraph's `StateGraph` to define nodes and edges for decision-making and action execution.
   - The graph alternates between language model responses and tool invocations based on the need for external actions.

2. **Integration with Tavily Search Results**:
   - The Tavily Search Results API is integrated for search-based tool functionality, allowing up to 4 results per query.

3. **ChatGroq Language Model**:
   - The assistant leverages ChatGroq with the `Gemma2-9b-It` model for generating responses and determining tool usage.

4. **Dynamic Workflow**:
   - Conditional edges within the graph allow the assistant to decide whether to take actions (invoke tools) or continue the conversation with the language model.

5. **User-Defined Prompt**:
   - A customizable system prompt ensures the assistant behaves as an intelligent research assistant.

---

## Prerequisites
1. **Python Libraries**:
   Ensure the following libraries are installed:
   - `langgraph`
   - `langchain_community`
   - `langchain_groq`
   - `IPython`

   Install any missing dependencies via:
   ```bash
   pip install langgraph langchain_core langchain_community langchain_groq IPython
   ```

2. **Environment Variables**:
   - Set your Tavily and Groq API keys as environment variables.
     ```python
     from google.colab import userdata
     tavily_api_key = userdata.get('tavily_api_key')
     os.environ['TAVILY_API_KEY'] = tavily_api_key
     groq_api_key = userdata.get('groq_api_key')
     ```

---

## Code Explanation

### Components

#### 1. **StateGraph**
- The assistant's workflow is managed by a `StateGraph` object.
- Two nodes are defined:
  - `llm`: Handles the language model's response generation.
  - `action`: Executes tool invocations based on the language model's outputs.
- Edges are configured to allow transitions between these states based on whether tools need to be invoked.

#### 2. **Agent Class**
- Encapsulates the functionality of the assistant.
- Handles state transitions and tool invocations.
- Core methods:
  - `call_openai`: Sends messages to the language model (ChatGroq).
  - `take_action`: Invokes tools based on the language model's outputs.

#### 3. **TavilySearchResults Tool**
- Integrated as a search tool.
- Configured with a maximum of 4 search results per query.

#### 4. **ChatGroq**
- A language model used for response generation and determining tool usage.

#### 5. **Custom Prompt**
- The system prompt guides the assistant's behavior and ensures it operates as a research assistant.

#### 6. **Graph Visualization**
- The graph's workflow is visualized using `pygraphviz`.
- Rendered as a PNG image with:
  ```python
  Image(abot.graph.get_graph().draw_png())
  ```

### Input/Output Example
1. Input:
   ```python
   messages = [HumanMessage(content="What is the weather in sf?")]
   result = abot.graph.invoke({"messages": messages})
   print(result['messages'][-1].content)
   ```
2. Output:
   - The assistant retrieves and displays weather information for San Francisco by using the Tavily search tool.

---

## How to Use

1. **Set Up Environment**:
   - Ensure all prerequisites are installed.
   - Configure your Tavily and Groq API keys as environment variables.

2. **Run the Code**:
   - Copy the provided code into a Python environment or Jupyter Notebook.
   - Execute the script to initialize the assistant.

3. **Query the Assistant**:
   - Send messages to the assistant using:
     ```python
     messages = [HumanMessage(content="Your Query Here")]
     result = abot.graph.invoke({"messages": messages})
     print(result['messages'][-1].content)
     ```

4. **Visualize Workflow**:
   - Generate a PNG visualization of the assistant's workflow:
     ```python
     Image(abot.graph.get_graph().draw_png())
     ```

---

## Troubleshooting

1. **Tavily API Key Error**:
   - Ensure your `TAVILY_API_KEY` is correctly set in the environment variables.
   - Validate the key with the Tavily API.

2. **Graph Rendering Error**:
   - Install `pygraphviz` if not already installed:
     ```bash
     pip install pygraphviz
     ```

3. **Empty or Repeated Output**:
   - Check the raw response content with:
     ```python
     print(repr(result['messages'][-1].content))
     ```
   - Sanitize the response if necessary.

---

### Future Improvements
- Enhance error handling for invalid or missing API keys.
- Add support for additional tools beyond Tavily Search Results.
- Optimize the assistant for low-latency responses.

---

### License
This project is provided as-is under the MIT License.

---

### Acknowledgments

- [LangChain](https://www.langchain.com/): For providing the foundational libraries.  
- [Tavily](https://tavily.com/): For the search tool integration.  
- [ChatGroq](https://www.groq.com/): For the language model support.  

------------------------------
-----------------------------
#  Agentic Search vs. Regular Search

This notebook provides a comparative exploration of regular and agentic search approaches. Depending on the use case—whether quick, structured answers or customizable web scraping—users can choose the method that best fits their needs.

---

## Introduction
This code illustrates two methods for querying and retrieving weather information for a specific location:

1. **Regular Search**: Utilizes search engines like DuckDuckGo (via the `duckduckgo_search` library) to retrieve weather-related information from external websites.
2. **Agentic Search**: Leverages the Tavily API to process queries and provide direct, structured answers through pre-trained AI models.

---

## Features
- **Regular Search:**
  - Web scraping with BeautifulSoup.
  - Retrieves links from DuckDuckGo.
  - Parses and cleans the content of a web page to extract relevant data.

- **Agentic Search:**
  - Uses the Tavily API to directly fetch structured, AI-driven results.
  - Provides concise answers with context.

---

## Setup

### Prerequisites
1. Install required Python libraries:
   ```bash
   pip install requests beautifulsoup4 duckduckgo_search pygments
   ```
2. Ensure you have the Tavily API key configured in Google Colab:
   ```python
   from google.colab import userdata
   tavily_api_key = userdata.get('tavily_api_key')
   os.environ['TAVILY_API_KEY'] = tavily_api_key
   ```
3. Ensure internet access is enabled for web scraping and API calls.

---

## How It Works

### Regular Search

1. **Search Query Formation**: A query is constructed dynamically based on user input (e.g., the city name).
   ```python
   query = f"what is the current weather in {city}? Should I travel there today?"
   ```

2. **DuckDuckGo Search**: The `DDGS` library fetches search results.
   ```python
   results = ddg.text(query, max_results=6)
   ```

3. **Web Scraping**: The content of the first search result is scraped using BeautifulSoup to extract weather-related data.
   ```python
   response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
   soup = BeautifulSoup(response.text, 'html.parser')
   ```

4. **Content Cleaning**: The scraped content is cleaned and structured.
   ```python
   weather_data = "\n".join(tag.get_text(" ", strip=True) for tag in soup.find_all(['h1', 'h2', 'h3', 'p'])
   ```

### Agentic Search

1. **API Query**: The Tavily API processes the query and returns structured results.
   ```python
   result = client.search(query, max_results=1)
   data = result["results"][0]["content"]
   ```

2. **Structured Output**: The returned JSON content is formatted for better readability.
   ```python
   formatted_json = json.dumps(json.loads(data.replace("'", '"')), indent=4)
   ```

---

## Comparative Analysis

| Feature               | Regular Search                             | Agentic Search                                |
|-----------------------|--------------------------------------------|-----------------------------------------------|
| **Ease of Use**       | Requires parsing and cleaning raw content. | Provides structured and ready-to-use answers. |
| **Accuracy**          | Relies on external sources and scraping.   | AI-driven, concise, and contextually accurate.|
| **Speed**             | Dependent on web scraping and parsing.     | Faster due to API-based direct answers.       |
| **Customization**     | Fully customizable scraping logic.         | Limited to the API’s capabilities.            |
| **Dependency**        | Requires DuckDuckGo and BeautifulSoup.     | Requires Tavily API access.                   |

---

#### Example Usage

### Regular Search
```python
query = "what is the current weather in Egypt?"
url = search(query)[0]
soup = scrape_weather_info(url)
print(weather_data)
```

### Agentic Search
```python
query = "what is the current weather in Egypt?"
result = client.search(query, max_results=1)
print(result["results"][0]["content"])
```

---

## Acknowledgments
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): For HTML parsing and web scraping.
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/): For accessing search engine results.
- [Tavily API](https://tavily.com/): For providing structured, AI-driven search capabilities.
- [Pygments](https://pygments.org/): For formatting JSON output.

---

# AI Agent - Essay Writer

## Overview
AI Agent - Essay Writer is an intelligent essay-writing assistant that generates high-quality essays based on user-provided topics. It uses a stateful AI workflow powered by LangGraph and integrates with Groq's AI model for text generation and Tavily for research queries.

## Features
- Generates structured essay outlines.
- Writes full essays based on outlines and user input.
- Provides critique and recommendations for improvements.
- Incorporates research-backed enhancements.
- Uses a feedback loop to refine essay drafts.
- Interactive Gradio UI for easy usage.

## Technologies Used
- **Python** for scripting and workflow management.
- **LangGraph** for managing AI agent states and workflow logic.
- **Langchain-Groq** for AI-powered text generation.
- **Tavily API** for gathering relevant research.
- **Gradio** for user-friendly web-based UI.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd ai-agent-essay-writer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API keys as environment variables:
   ```bash
   export GROQ_API_KEY="your_groq_api_key"
   export TAVILY_API_KEY="your_tavily_api_key"
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Usage
1. Open the Gradio UI in your browser.
2. Enter an essay topic in the input box.
3. Click the **Generate Essay** button.
4. View and refine the generated essay in the output box.

## Future Improvements
- Implement support for multiple AI models.
- Enhance UI with additional customization features.
- Improve feedback mechanism for refining essay quality.
---------------------------------------------------------------------------


