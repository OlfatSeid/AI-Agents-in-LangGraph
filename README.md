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

data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWMAAAFtCAYAAADSyAuRAAAABmJLR0QA/wD/AP+gvaeTAAAgAElEQVR4nOzdeVhU5f/G8fewyg6CuKKICioqYmKL4lKaqeVSmrmn+Q1TM3+VlaXmlqWWleZulltlau67ueaOYi6QgAougIjsINvM/P6YRMldYc6Z4fO6rrkYhpk5NzrcPDxzznM0er1ejxBCCCWlWCidQAghBEgZCyGECkgZCyGEClgpHUCoQ2pqKtnZ2WRlZZGeno5eryc1NbXIfbKzs8nNzS1ym6OjI9bW1oWfW1lZ4eTkhKWlJc7Ozjg5OWFvb4+Dg4NRvg8hTJWUsZnRarUkJCQQGxtLYmIi169f5+rVqyQlJXH9+nWuXUviWtI1kpKSyMzMJDs7m+ysLKNkc3V1w87eDicnJ9zdPShXzoNyHh54enri4eFReKlcuTJeXl6ULVvWKLmEUAON7E1hWvR6PZcvXyYyMpKoqChiYmK4dOkSMbEXuXTpIvHx8RTk5xfe397REVd3D5zd3HF0K4ujixvObmVxdiuLnaMjNmXsKGNvj4OTMzZl7LC1s8PBydnwWCdnNBa3ZrKsbWywLWNXJE9Wejp6br2E8nNzyMvJQavVciMrkxuZGeTeuEFuzg2y0tPIvXGDG1mZZKQkk56STGZqMunJ10lPSSYt+Tp5t4287eztqVq1KlW9quLlVYWqVavi4+ODr68vvr6+uLm5ldQ/sxDGliJlrFJarZbIyEhOnDjBmTNniIyM5Oy/BXwjOxsAJxdXPCt74V6hEh6VKuNeoRLuFSriUbEy5SpVxtXDE6vbphBMQU52FknxcVy/Gs/1hHiS4i5zLf4KKVfjSYqPI+HSRfLzDIXt7lEOX19f6tT2o1atWjRo0ICGDRtSqVIlhb8LIR6ZlLEaFBQUcOLECY4fP05YWBjHw8I4deoUN7KzsbKypopPDSp4+1DR24dK1XyoVL0Glbx9cC7rrnR0o9NptSTFXyEu5rzhcuEcCbHnibtwnqtXLgFQztOTwIaBBAY2JDAwkKCgIHx8fBROLsR9SRkrITMzkxMnTrB//3727dvHvn1/kZ6ehr2jI5W8fahcw5ca/g3w8W9ADf8G2JQpo3Rkk5CdmUHs2QjOnznJ5ehIrpyLJOrU3+Tl5eJZvgJBQY0JbtaMpk2bEhQUhK2trdKRhbhJytgYCgoKOHDgAFu2bGHzli2cOnkSrVZLZW8f/AKD8GsURO1GQVT2qYlGo1E6rlnJz83l3JmTRBw7wtmwo5wNCyU9JRl7BweCmwXTrt1LtGvXDl9fX6WjitJNyrikJCYmsn79ejZv3sz27TtIT0+jsnd1GjRtSf1nmuHXqDGu7uWUjlnq6PV6rpyLIuL4UU4e2Mupg/vISEvFu3p12rdrR/v27WndurWMmoWxSRkXp9TUVNatW8fvv69g67atWFpaUrtRE+o/G0yD54Kp4d9A6YjiP3RaLRf+OcPJA/s4vns7/4SF4ujoRKdOHenWrRtt27bFxsZG6ZjC/EkZP6mCggLWrVvHjwsXsn37djQaDU+1eIFnX+pI4+fb3LErmFC36wnxHNiynoOb13H27+OUdXfn9W7dCAkJoWHDhkrHE+ZLyvhxJSQksGDBAmbPmUNCfDyBzVrS7OUuNH7+RewdnZSOJ4pB4uWL7N+0jr3rVnAxOopnn32OoUOH0LVrVxkti+ImZfyooqKiGD9hAsuXL8fOwZFWr75B2zf6UN6rmtLRRAnR6/WcOXKArb8s4vCfW3BzK8vw94YxbNgwnJzkF68oFlLGD+vChQtMmDCBJUuWULFadToNHEyz9p2xljd6SpXkqwls/W0xm5cuxNbGhk8+/oghQ4Zgb2+vdDRh2qSMHyQzM5NRo0Yxc9YsPCtVoevg/yP45S5YWFoqHU0oKDMtlbU/zmbzsoU4OToxdcpk+vbtq3QsYbqkjO9n27Zt/O/tt0lNz6Dn/43k+de6Y2kpayuJW9KTr/P7zGls/XURrVu3Yd68uVSrJlNW4pHJmT7uJicnh4EDB9K2bVu86gbw3YbdtHm9lxSxuINzWXcGjv6CicvWEHHuPP7+9fjpp5+UjiVMkJTxfyQmJvL88y/w+8pVfDzzJ97/dg4u7h5KxzKa70cM5bXalQjdvd0stmMsfoGNmbp6Oy/27Mdbb73FRx99hE6nUzqWMCEy1LvNP//8w0vt2pGv1/DFr+uo7FNT6UhGlXr9Gge2rDeb7RibtY0NvT/4jKq+dfjusw+IjIxi+fLf5Gg+8VBkzvhfsbGxPPdcU1wqVOLjWT/j5Go+a+WeOvgX6xfN41LUWVKuXcXByQXvOv607z2Ap1q2BmBMn9c4c/TgHY8dOWcRjVu2AeBsWCjrFs4h/NhhstLTcS9fAb/AxnR/90MqVqte+JhvP3iHvzauxdrGhsVH/uH7j94lbN8uegwbwdGd2x64HXNwNiyUSSF9eLVLZxb9/LPScYT6pcjIGMjLy+O117pi4+TMp3OXYP/v4urm4MiOLUwZNhD9bX8yp16/xom/dnPir928/fmXtO3R74HPc3zvTr5650202oLC2xKvXCLxyiVCd21nyqotVPI2LFNp8+9Rh/l5eayY9S2Htm0EIDfnRnF+a6rmF9iY/5s2my9C+lC/Xj0+/PBDpSMJlZM5Y+Crr74i/J8IPpy+wKyKGGDNj7PQ63RUrVWb2TsO8fuZiyzYF0bjlm1wcffg8I4t6PV6xi9ZxcDRXxQ+buScRaz6J65wtLr110XY2ttjZW3NxGVrWH4qlvemzADgRlYmG36eV/jY21eeO7BlPeMWreC3kzF06DvwgdsxJw2btaTfR2P45JNPCAsLUzqOULlSPzJOSkriq8mT6Tr4/SJ/apuLzDTDSUVzbmSj0+mwtLTCrVx5Rs5Z9EjPM3J20fvrdTqefekVfhj5f2i1BVw6F3nXx7Xu1ot6TzcFDHOqpU2HvgM5tG0jH3/8Cdu2bVU6jlCxUl/GixcvxtLKmna9+ysdpUQ0av48V85Hk3j5IkNefI7KPjXxa/gU9Z8N5uk27R56IaPsjHTWL5rPgc3rSLxyibycnCJfz8/Lu+vj6jzV5Im/B1Om0Wh4NWQYk0L6EB0dTc2apetNYfHwSn0Zb9myladatjbb1dX6fPgZOdnZ7PxjOdqCfK6cj+bK+Wh2/rEcZ7eyvDf1Bxo2a3nf59BptYwf2JOov48XuV2j0fCg939L46mh/qth0xY4ODmzdetWKWNxT6V+zjg8IpzqdeopHaPEWFpZM2j8FBbsC+P/vplN+94DqOZbB4D0lGSmDH2L9JTk+z5HeOihwiKuUqMW09b9ye9nLrLizKUHHghjYVHqX2JYWFri7VeHiIgIpaMIFSv1PylZWdnYloJFXpzdytKsQyfeGjWRaev+pPcHnwGGPRxi/wm/4/467a29LxKvXC68/ly7jlTzrYOlpRXRp04U2bvicdy+HXNWxsGRzMxMpWMIFSv1Zezh4U7qtUSlY5SI1KREPuvZiQFNG7Bs2pdkpqeh1+nITEsl47bRsJtneQBsbG+d+PTEX7vJz8sjLycH9/IVCm+POHaY7Ix0zoefYtaoD9H8O/JNSUxAp9U+VK57bcecpV5LxNPTU+kYQsVKfRk/3aQJ/xw7onSMEuHq4YlbufKkXU/ij3kz6NekDl3rVqHf03VZu3A2AM06dKZKjVoAeNeuW/jYrb8u4o0G3vy56ldqP9UEj4qVAMMBJH2CajPi1bZotQV0HjgYgKT4ON5u2ZizJ449MNe9tmOustLTuXA2nKCgIKWjCBUr9WXctWtXTh3eT8LFGKWjlIj3p81mwGcT8AtsjLNbWSytrHH18MQvsDEDR39RuK8wQI16AfQc/jGu7uWwsrbGs7IX5SpXwbaMHaPmL6PBc8HYOTrh7FaWlp27MXHpajoNeIdGLV7A1cMTZ7ey2Dk4PDDTvbZjrnatXo5dGTvatm2rdBShYqX+cOiCggLq1PWnfA0/3v9urtJxhJnJSk9nWLtmDOjXl2+++UbpOEK9ZAlNKysrZkz/ngNbN7Bvw2ql4wgzotfrmTtmBGWsrRk1apTScYTKlfr9jAFeeukl3nvvPWaP+gCPipWNeqDCudN/81HXdiXy3Ka0+I45/jv8Nn0qh3dsZuvWrbi5mc/CU6JklPppipu0Wi1du3Vj67ZtDP9mlsmUmFAfvU7H4qkTWf/zXH788Uf69zfPoztFsZJpipssLS1Z8fvv9O/Xj8lDBrB6/kylIwkTlHsjm6nDBrLll59YvHixFLF4aDJNcRsrKytmzpyJt7c3n3zyCbFnwxnw6Xg5pFc8lMi/jzFn1IdkpSSza+dOnnvuOaUjCRMiI+O7GDFiBJs2bSLm72MMf7kle9etUjqSULHcG9ksnDSGz3p2pmZVL0JDj0oRi0cmc8b3kZGRwaeffsqsWbOo1+Q53hj+MX4Nn1I6llAJrbaAPWtWsmLmNPJvZDNt2jf069evyHrOQjykFCnjh3Dw4EE++uhj/vprH0+1eIHu735IjXoBSscSCtHrdOzbsJqVs77l6pVLDOjfn/Hjx1O+fHmlownTJWX8KLZt28ao0WMIPXqEhs1a8FLP/jRq/jwWlpZKRxNGkJ2Rzq41K9j6y88kXIyhd+/ejBkzBh8fH6WjCdMnZfw4Nm7cyPffT2fHju14Vq5Cm9f78ELXHvJGn5m6EHGGrb/+zL4Nq7HUWNC7dy/ef/99fH19lY4mzIeU8ZOIjo5mwYIFzJu/gLS0VPwCGtGiczeatu+EvaOT0vHEE0iKv8Lh7Zs5tHUD4ceOULOWLwPfGsD//vc/ypYtq3Q8YX6kjItDdnY2f/zxB78tX862bdvQaDQ0av48z77UkYbBLXF0dlE6ongICRdjOLpzGwc3r+Ps38cp6+7O69260aNHD4KDg+WNOVGSpIyLW0pKiqGYf1vO7t270On1+AU0omFwKwKDW+FTt37hGsBCWbk5Nzh9aD9h+3bx91+7iYu9gIuLK126dKZ79+60bt0aKyvZFV8YhZRxSUpNTWXHjh1s2bKFTZs3Ex8Xh5u7B3WCnqV2oyBqP9UE79p1H3jqIlE8sjMziDxxjH/CQvnn2GHOhoWSn5dHg4AA2rdrx0svvcRzzz0nBSyUIGVsTCdPnmTbtm3s2buXA/sPkJx8HTsHB3wDGuHXqAk16jWgeu16uFeoqHRUk6fVFnDlfDQxEWeI/Ps4Z48fJSYyAp1WS42aNWnWtCnPP/88bdu2lV3ShBpIGStFr9cTERHBX3/9xf79+/lr/37OnzsHgEtZd7xr++Ndpx7etetSzbcOlbx9sLa1VTi1OmWkphiK958zhkvEGWIjI8jLzcXaxoaAgACaNW1KcHAwzz33HBUqVHjwkwphXFLGapKWlsaJEyf4+++/OXHiBMfDwggPDyc/Lw8LCwvKVaxMRW8fKnr7UNmnJpW8fShX2QuPCpWwKVPmwRswYZlpqVxPiCc+9jxxMeeJjzlP3IVzxMWcLzy7tYuLKwENA2gUGEjDhg0JCAjA398fa2trhdML8UBSxmqXn59PVFQUZ8+eJTIyksjISCL+OcvZs2dJvp5UeD9Xd3fcy1eibIWKeFSsjHuFSriV88TJ1Q1nt7K4eJTD2a0sZewffFokY0pPSSYjJbnwY1pyEsmJV0mKu0zy1QSSr8aTeOUSOTduAGBhYYFX1ar41vKldm0//Pz88PX1xdfXl2rVqin83Qjx2KSMTVlycjKxsbFcvny58OPly5e5EBPLpUsXSUxMJPc/Z122sbXFpax7YTHblCmDnaMzZeztsbWzp4y9PXaOTlhYWGJlZUWZIue00+Dg7Fz4mU6r5UZW0dPPZ6alAZCfm0Nuzg2y0tPJvZFNbs4NcrKyyMnOJDcri7SUZNJSku84o7STkzOVq1TGq4oXXl5VqFq1KlWrVqVKlSpUqVIFHx8fbGW6RpgfKWNzl5WVRVJSElevXiUpKYmkpCSuX79OUlISmZmZZGdnk5aWRkZGJplZWWRlZZKamoperycnJ4ecG7fKvKCggMzMjMLPNRoNLi6uRbbn5OyEpaUlNjY2ODg4UNbNDXsHBxzs7XF2dsbZ2RkHBwc8PDzw8PDA09Oz8LqHhwc2NjZG+7cRQkWkjMWja9iwIS+//DITJ05UOooQ5kLO9CGEEGogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECogZSyEECqg0ev1eqVDCPX65ZdfOHnyZJHbVq5cSdWqVWnSpEmR27t3705gYKAx4wlhLlKkjMV9LViwgP/973/Y2Nig0Wjueh+tVotWq+Xy5ctUqlTJyAmFMAtSxuL+UlJSKF++PPn5+fe8j4WFBc2aNWPPnj1GTCaEWUmROWNxX25ubrRt2xYrK6t73kej0dC3b18jphLC/EgZiwfq1asXWq32nl/XaDR06dLFiImEMD9SxuKBOnbsSJkyZe76NSsrK1566SXKli1r5FRCmBcpY/FA9vb2dOnSBWtr6zu+ptVq6d27twKphDAvUsbiofTs2fOub+LZ2try8ssvK5BICPMiZSweStu2bXFzcytym7W1Na+++ioODg4KpRLCfEgZi4di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

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

## Future Improvements
- Enhance error handling for invalid or missing API keys.
- Add support for additional tools beyond Tavily Search Results.
- Optimize the assistant for low-latency responses.

---

## License
This project is provided as-is under the MIT License.

---

## Acknowledgments
- **LangChain**: For providing the foundational libraries.
- **Tavily**: For the search tool integration.
- **ChatGroq**: For the language model support.


