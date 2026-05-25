# 🚀 Builders Skill Sprint Challenges - Complete Setup Guide

## 📋 Overview

This repository contains **5 completed AI agent challenges** using the Strands SDK. All challenges have been fully implemented and are ready to run!

---

## 🎯 Challenges Summary

| Challenge | Description | Model | Key Features |
|-----------|-------------|-------|--------------|
| **Challenge 1** | First AI Agent | Ollama (Local) | Basic agent setup |
| **Challenge 2** | Tools Integration | Amazon Nova Pro | Calculator, Weather, Age Calculator |
| **Challenge 3** | Persistent Memory | Amazon Nova Pro | FAISS-based memory |
| **Challenge 4** | Full Agent | Amazon Nova Pro | Tools + Memory + Streaming |
| **Challenge 5** | MCP Chatbot | Amazon Nova Pro | AWS Documentation Expert |

---

## 🛠️ Prerequisites

### 1. Python Environment
```bash
# Python 3.8 or higher required
python --version
```

### 2. Install Dependencies

```bash
# Core dependencies
pip install strands-agents
pip install strands-tools

# For Challenge 1 (Ollama)
# Download and install Ollama from: https://ollama.ai

# For Challenges 2-5 (AWS Bedrock)
pip install boto3
aws configure  # Set up AWS credentials

# For Challenge 3-4 (Memory)
pip install faiss-cpu

# For Challenge 5 (MCP)
pip install awslabs.aws-documentation-mcp-server

# For weather functionality
pip install requests
```

### 3. AWS Setup (Challenges 2-5)

```bash
# Configure AWS credentials
aws configure

# Ensure you have access to Amazon Nova Pro in Bedrock
# Region: us-east-1 (or your preferred region)
# Model: us.amazon.nova-pro-v1:0
```

### 4. Ollama Setup (Challenge 1 Only)

```bash
# Install Ollama from https://ollama.ai
# Then pull the required model:
ollama pull llama3.2:3b

# Start Ollama server (keep this running in a separate terminal):
ollama serve
```

---

## 🏃 Running Each Challenge

### Challenge 1: Your First AI Agent (Ollama - Local)

**Prerequisites:**
- Ollama installed and running (`ollama serve`)
- Model `llama3.2:3b` pulled

**Run:**
```bash
cd April-2026/challenge-1-first-agent
python starter.py
```

**Expected Output:**
```
🤖 Agent: Python is a high-level, interpreted programming language...
✅ Challenge 1 complete!
```

**What it does:**
- Creates a local AI agent using Ollama
- Asks a question about Python programming
- Demonstrates basic agent setup

---

### Challenge 2: Adding Tools to Your Agent

**Prerequisites:**
- AWS credentials configured
- Amazon Nova Pro access in Bedrock

**Run:**
```bash
cd April-2026/challenge-2-tools
python starter.py
```

**Expected Output:**
```
🧮 Math test:
714

🌤️ Weather test:
Weather in Chennai: Partly cloudy, 33°C...

🎂 Age test:
Age: 24 years old (born on 2000-05-15)

✅ Challenge 2 complete!
```

**What it does:**
- Demonstrates tool integration
- Calculator tool for math operations
- Weather tool using wttr.in API
- Age calculator tool using datetime

---

### Challenge 3: Agent with Persistent Memory

**Prerequisites:**
- AWS credentials configured
- `faiss-cpu` installed

**Run:**
```bash
cd April-2026/challenge-3-memory
python starter.py
```

**Example Interaction:**
```
You: Remember that my name is Ravi and I love biryani
Agent: ✅ I'll remember that!

You: What's my name and what food do I like?
Agent: Your name is Ravi and you love biryani!

You: quit
```

**What it does:**
- Stores user preferences in FAISS vector database
- Memories persist across sessions
- Demonstrates mem0_memory tool usage

**Testing Persistence:**
1. Run the program and store some facts
2. Type `quit` to exit
3. Run the program again
4. Ask about the stored facts - they should still be there!

---

### Challenge 4: The Full Agent (Tools + Memory + Streaming)

**Prerequisites:**
- AWS credentials configured
- `faiss-cpu` installed

**Run:**
```bash
cd April-2026/challenge-4-full-agent
python starter.py
```

**Example Interaction:**
```
You: Remember my name is Priya and I'm from Madurai
🔧 Using tool: mem0_memory
Agent: ✅ Stored!

You: What's the weather in my city?
🔧 Using tool: mem0_memory
🔧 Using tool: weather
Agent: Weather in Madurai: Sunny, 38°C...

You: How old is someone born on 2002-03-15? Also what's 365 * 24?
🔧 Using tool: age_calculator
🔧 Using tool: calculator
Agent: 24 years old. 365 × 24 = 8,760 hours in a year!

You: quit
```

**What it does:**
- Combines all features: tools + memory + streaming
- Real-time streaming responses
- Shows tool usage as it happens
- Full conversational agent

---

### Challenge 5: AWS Documentation Expert (MCP-Powered)

**Prerequisites:**
- AWS credentials configured
- AWS Documentation MCP server installed

**Install MCP Server:**
```bash
pip install awslabs.aws-documentation-mcp-server
```

**Run:**
```bash
cd April-2026/challenge-5-innovate-mcp-chatbot
python starter.py
```

**Example Interaction:**
```
You: Explain what AWS Lambda is and how it works
🔍 Searching AWS docs using: search_documentation...
Agent: AWS Lambda is a serverless compute service...

You: Remember that I'm learning about serverless architecture
Agent: ✅ I'll remember that you're learning about serverless!

You: What are the best practices for Lambda functions?
🔍 Searching AWS docs...
Agent: Here are the key best practices for Lambda...

You: quit
```

**What it does:**
- Connects to AWS Documentation MCP server
- Searches real AWS documentation
- Provides accurate, up-to-date AWS information
- Remembers your learning journey
- Streaming responses with tool usage indicators

**Innovation Highlights:**
- ✨ Real-time AWS documentation search
- ✨ Streaming responses for better UX
- ✨ Persistent memory for personalized learning
- ✨ Comprehensive AWS knowledge base access

---

## 🧪 Testing All Challenges

### Quick Test Script

Create a file `test_all.sh`:

```bash
#!/bin/bash

echo "Testing Challenge 1..."
cd April-2026/challenge-1-first-agent
python starter.py
echo ""

echo "Testing Challenge 2..."
cd ../challenge-2-tools
python starter.py
echo ""

echo "Testing Challenge 3..."
cd ../challenge-3-memory
echo "Remember that my name is Test User" | python starter.py
echo ""

echo "Testing Challenge 4..."
cd ../challenge-4-full-agent
echo "What is 10 * 5?" | python starter.py
echo ""

echo "Testing Challenge 5..."
cd ../challenge-5-innovate-mcp-chatbot
echo "What is AWS Lambda?" | python starter.py
echo ""

echo "✅ All challenges tested!"
```

---

## 🐛 Troubleshooting

### Challenge 1 Issues

**Problem:** `Connection refused to localhost:11434`
**Solution:** Make sure Ollama is running: `ollama serve`

**Problem:** `Model not found: llama3.2:3b`
**Solution:** Pull the model: `ollama pull llama3.2:3b`

### Challenges 2-5 Issues

**Problem:** `AWS credentials not found`
**Solution:** Run `aws configure` and enter your credentials

**Problem:** `Access denied to Amazon Nova Pro`
**Solution:** 
1. Go to AWS Bedrock console
2. Navigate to Model access
3. Request access to Amazon Nova Pro
4. Wait for approval (usually instant)

**Problem:** `Module 'faiss' not found`
**Solution:** `pip install faiss-cpu`

### Challenge 5 Issues

**Problem:** `MCP server not found`
**Solution:** `pip install awslabs.aws-documentation-mcp-server`

**Problem:** `MCP connection timeout`
**Solution:** Check your internet connection and AWS credentials

---

## 📝 Code Modifications Summary

### Challenge 1
- ✅ Imported `Agent` and `OllamaModel`
- ✅ Created Ollama model instance
- ✅ Created agent with system prompt
- ✅ Added question and response handling

### Challenge 2
- ✅ Created `weather()` tool with wttr.in API integration
- ✅ Created `age_calculator()` tool with datetime logic
- ✅ Created agent with all tools (calculator, weather, age_calculator)
- ✅ Added test cases for all tools

### Challenge 3
- ✅ Imported `mem0_memory` from strands_tools
- ✅ Created agent with memory tool
- ✅ Implemented interactive chat loop
- ✅ Added proper input handling and exit conditions

### Challenge 4
- ✅ Created streaming callback handler
- ✅ Implemented weather and age_calculator tools
- ✅ Created full agent with all tools + memory + streaming
- ✅ Added interactive chat loop with streaming support
- ✅ Enhanced system prompt with emojis and personality

### Challenge 5
- ✅ Built complete AWS Documentation Expert from scratch
- ✅ Integrated AWS Documentation MCP server
- ✅ Combined MCP tools with mem0_memory
- ✅ Added streaming callback for better UX
- ✅ Created comprehensive system prompt
- ✅ Implemented interactive chat loop
- ✅ Added error handling and user guidance

---

## 🎓 Learning Outcomes

After completing these challenges, you now understand:

1. **Basic Agent Setup** - How to create and configure AI agents
2. **Tool Integration** - How to add custom and built-in tools
3. **Persistent Memory** - How to use FAISS for long-term memory
4. **Streaming Responses** - How to implement real-time streaming
5. **MCP Integration** - How to connect to Model Context Protocol servers
6. **AWS Bedrock** - How to use Amazon Nova Pro model
7. **Local Models** - How to run agents locally with Ollama

---

## 🚀 Next Steps

1. **Experiment** - Modify the agents to add new features
2. **Combine** - Mix and match tools from different challenges
3. **Create** - Build your own custom tools and agents
4. **Deploy** - Consider deploying your agents as web services
5. **Share** - Submit your Challenge 5 innovation!

---

## 📚 Resources

- [Strands SDK Documentation](https://strandsagents.com)
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Ollama Documentation](https://ollama.ai/docs)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)
- [AWS MCP Servers](https://github.com/awslabs/mcp)

---

## 🎉 Congratulations!

You've successfully completed all 5 Builders Skill Sprint Challenges! 🏆

All code is production-ready, well-commented, and follows best practices.

Happy building! 🚀
