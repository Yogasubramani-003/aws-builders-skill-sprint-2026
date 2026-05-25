# 🚀 Builders Skill Sprint Challenges - April 2026

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Strands SDK](https://img.shields.io/badge/Strands-SDK-green.svg)](https://strandsagents.com)
[![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-orange.svg)](https://aws.amazon.com/bedrock/)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)]()

## 📖 About

This repository contains **5 fully completed AI agent challenges** built with the Strands Agents SDK. Each challenge progressively builds your skills in creating intelligent AI agents, from basic setup to advanced MCP-powered applications.

**All challenges are production-ready and fully functional!** ✅

---

## 🎯 Challenges Overview

### Challenge 1: Your First AI Agent ⭐
**Model:** Ollama (Local - llama3.2:3b)  
**Difficulty:** Beginner  
**Learn:** Basic agent setup, local model integration

Create a simple AI agent that runs 100% locally on your machine using Ollama.

**Key Concepts:**
- Agent initialization
- System prompts
- Local model configuration

---

### Challenge 2: Adding Tools to Your Agent ⭐⭐
**Model:** Amazon Nova Pro (Bedrock)  
**Difficulty:** Intermediate  
**Learn:** Tool integration, custom tool creation

Give your agent superpowers with calculator, weather, and age calculator tools.

**Key Concepts:**
- Built-in tools (calculator)
- Custom tool creation with `@tool` decorator
- Tool selection and execution

---

### Challenge 3: Agent with Persistent Memory ⭐⭐
**Model:** Amazon Nova Pro (Bedrock)  
**Difficulty:** Intermediate  
**Learn:** Persistent memory, FAISS vector store

Build an agent that remembers facts across sessions using FAISS.

**Key Concepts:**
- Conversation history vs persistent memory
- Vector-based memory storage
- Memory retrieval and recall

---

### Challenge 4: The Full Agent ⭐⭐⭐
**Model:** Amazon Nova Pro (Bedrock)  
**Difficulty:** Advanced  
**Learn:** Streaming, combining features

Combine everything: tools + memory + streaming for a complete agent experience.

**Key Concepts:**
- Streaming responses
- Callback handlers
- Multi-tool coordination
- Full-featured conversational AI

---

### Challenge 5: MCP-Powered Innovation 🚀
**Model:** Amazon Nova Pro (Bedrock)  
**Difficulty:** Advanced  
**Learn:** MCP integration, creative problem-solving

Build an innovative AWS Documentation Expert that connects to MCP servers.

**Key Concepts:**
- Model Context Protocol (MCP)
- External tool integration
- Real-world application development
- Creative agent design

**Innovation:** Combines AWS documentation search with persistent memory for personalized learning assistance.

---

## 🛠️ Quick Start

### 1. Install Dependencies

```bash
# Clone the repository (if not already done)
git clone <repository-url>
cd builders-skill-sprint-challenges-main

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Set Up Prerequisites

**For Challenge 1 (Ollama):**
```bash
# Install Ollama from https://ollama.ai
ollama pull llama3.2:3b
ollama serve  # Keep running in separate terminal
```

**For Challenges 2-5 (AWS Bedrock):**
```bash
# Configure AWS credentials
aws configure

# Ensure Amazon Nova Pro access in Bedrock console
# Region: us-east-1 (or your preferred region)
```

### 3. Run Any Challenge

```bash
# Example: Run Challenge 1
cd April-2026/challenge-1-first-agent
python starter.py

# Example: Run Challenge 5
cd April-2026/challenge-5-innovate-mcp-chatbot
python starter.py
```

---

## 📁 Repository Structure

```
builders-skill-sprint-challenges-main/
├── README.md                          # This file
├── SETUP_AND_RUN.md                   # Detailed setup guide
├── requirements.txt                   # Python dependencies
└── April-2026/
    ├── challenge-1-first-agent/
    │   ├── README.md                  # Challenge instructions
    │   └── starter.py                 # ✅ Complete implementation
    ├── challenge-2-tools/
    │   ├── README.md
    │   └── starter.py                 # ✅ Complete implementation
    ├── challenge-3-memory/
    │   ├── README.md
    │   └── starter.py                 # ✅ Complete implementation
    ├── challenge-4-full-agent/
    │   ├── README.md
    │   └── starter.py                 # ✅ Complete implementation
    └── challenge-5-innovate-mcp-chatbot/
        ├── README.md
        └── starter.py                 # ✅ Complete implementation
```

---

## 🎓 What You'll Learn

| Skill | Challenges |
|-------|-----------|
| **Agent Basics** | 1 |
| **Tool Integration** | 2, 4 |
| **Custom Tools** | 2, 4 |
| **Persistent Memory** | 3, 4, 5 |
| **Streaming Responses** | 4, 5 |
| **MCP Integration** | 5 |
| **AWS Bedrock** | 2, 3, 4, 5 |
| **Local Models** | 1 |

---

## 💡 Features Implemented

### Challenge 1
- ✅ Ollama model integration
- ✅ Basic agent setup
- ✅ System prompt configuration
- ✅ Simple question-answer flow

### Challenge 2
- ✅ Calculator tool (built-in)
- ✅ Weather tool (custom, wttr.in API)
- ✅ Age calculator tool (custom, datetime)
- ✅ Tool selection and execution
- ✅ Multiple test cases

### Challenge 3
- ✅ mem0_memory integration
- ✅ FAISS vector store
- ✅ Interactive chat loop
- ✅ Persistent memory across sessions
- ✅ Memory storage and retrieval

### Challenge 4
- ✅ All tools from Challenge 2
- ✅ Memory from Challenge 3
- ✅ Streaming callback handler
- ✅ Real-time response streaming
- ✅ Tool usage indicators
- ✅ Enhanced system prompt with personality
- ✅ Full conversational experience

### Challenge 5
- ✅ AWS Documentation MCP server integration
- ✅ Real-time documentation search
- ✅ Streaming responses
- ✅ Persistent memory for learning journey
- ✅ Comprehensive error handling
- ✅ User-friendly interface
- ✅ Creative and innovative design

---

## 🧪 Testing

Each challenge has been tested and verified to work correctly. See [SETUP_AND_RUN.md](SETUP_AND_RUN.md) for detailed testing instructions.

**Quick Test:**
```bash
# Test Challenge 1
cd April-2026/challenge-1-first-agent && python starter.py

# Test Challenge 2
cd ../challenge-2-tools && python starter.py

# Test Challenge 3 (interactive)
cd ../challenge-3-memory && python starter.py

# Test Challenge 4 (interactive)
cd ../challenge-4-full-agent && python starter.py

# Test Challenge 5 (interactive)
cd ../challenge-5-innovate-mcp-chatbot && python starter.py
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue:** Ollama connection refused  
**Solution:** Ensure `ollama serve` is running

**Issue:** AWS credentials not found  
**Solution:** Run `aws configure` with your credentials

**Issue:** Amazon Nova Pro access denied  
**Solution:** Request model access in AWS Bedrock console

**Issue:** Module not found errors  
**Solution:** `pip install -r requirements.txt`

See [SETUP_AND_RUN.md](SETUP_AND_RUN.md) for detailed troubleshooting.

---

## 📚 Documentation

- **[SETUP_AND_RUN.md](SETUP_AND_RUN.md)** - Comprehensive setup and running guide
- **Individual Challenge READMEs** - Specific instructions for each challenge
- **[Strands SDK Docs](https://strandsagents.com)** - Official Strands documentation
- **[AWS Bedrock Docs](https://docs.aws.amazon.com/bedrock/)** - AWS Bedrock documentation

---

## 🎨 Code Quality

All implementations follow best practices:

- ✅ Clean, readable code
- ✅ Comprehensive comments
- ✅ Error handling
- ✅ Type hints where appropriate
- ✅ Consistent coding style
- ✅ Production-ready quality

---

## 🚀 Next Steps

1. **Run all challenges** to see them in action
2. **Experiment** with different prompts and questions
3. **Modify** the code to add your own features
4. **Create** new custom tools
5. **Build** your own innovative agents
6. **Share** your Challenge 5 creation!

---

## 📝 Git Commands for Submission

```bash
# Stage all changes
git add .

# Commit with descriptive message
git commit -m "Complete all 5 Builders Skill Sprint Challenges

- Challenge 1: Implemented Ollama-based local agent
- Challenge 2: Added calculator, weather, and age calculator tools
- Challenge 3: Integrated persistent memory with FAISS
- Challenge 4: Combined tools, memory, and streaming
- Challenge 5: Built AWS Documentation Expert with MCP integration

All challenges tested and verified working."

# Push to repository
git push origin main
```

---

## 🏆 Challenge 5 Submission

**Project:** AWS Documentation Expert  
**Description:** An intelligent chatbot that searches AWS documentation in real-time, provides accurate answers about AWS services, and remembers your learning journey using persistent memory.

**Innovation Highlights:**
- Real-time AWS documentation search via MCP
- Streaming responses for better user experience
- Persistent memory for personalized learning
- Comprehensive AWS knowledge base access

**Screenshot:** *(Take a screenshot of your agent in action)*

**Submit at:** [https://www.awsugmdu.in/](https://www.awsugmdu.in/)

---

## 🤝 Contributing

This is a completed challenge repository. Feel free to:
- Fork and experiment
- Add new features
- Create your own challenges
- Share improvements

---

## 📄 License

This project is part of the Builders Skill Sprint program.

---

## 🙏 Acknowledgments

- **Strands SDK Team** - For the excellent agent framework
- **AWS** - For Bedrock and Nova Pro model
- **Ollama** - For local model support
- **AWS UG MDU** - For organizing the Builders Skill Sprint

---

## 📞 Support

For questions or issues:
1. Check [SETUP_AND_RUN.md](SETUP_AND_RUN.md) for detailed guides
2. Review individual challenge READMEs
3. Consult [Strands documentation](https://strandsagents.com)
4. Visit [AWS UG MDU](https://www.awsugmdu.in/)

---

**Built with ❤️ for the Builders Skill Sprint Challenge**

🎉 **All 5 challenges completed successfully!** 🎉
