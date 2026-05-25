# 🚀 Quick Start Guide - Get Running in 5 Minutes!

This is the fastest way to get started with the Builders Skill Sprint Challenges.

---

## ⚡ Super Quick Setup (Copy & Paste)

### Step 1: Install Python Dependencies
```bash
cd builders-skill-sprint-challenges-main
pip install strands-agents strands-tools boto3 faiss-cpu requests
```

### Step 2: Choose Your Path

#### 🎯 Path A: Start with AWS Bedrock (Challenges 2-5)
**Best if you have AWS credentials**

```bash
# Configure AWS
aws configure
# Enter your AWS Access Key ID, Secret Key, and Region (us-east-1)

# Run Challenge 2 (easiest to start)
cd April-2026/challenge-2-tools
python starter.py
```

#### 🎯 Path B: Start with Ollama (Challenge 1)
**Best if you want to run locally first**

```bash
# Install Ollama from https://ollama.ai
# Then run:
ollama pull llama3.2:3b
ollama serve  # Keep this running

# In another terminal:
cd April-2026/challenge-1-first-agent
python starter.py
```

---

## 🎮 Try Each Challenge

### Challenge 1: Local AI Agent
```bash
cd April-2026/challenge-1-first-agent
python starter.py
```
**What happens:** Agent answers a question about Python  
**Time:** 10 seconds

---

### Challenge 2: Agent with Tools
```bash
cd April-2026/challenge-2-tools
python starter.py
```
**What happens:** Agent uses calculator, weather, and age tools  
**Time:** 30 seconds

---

### Challenge 3: Agent with Memory
```bash
cd April-2026/challenge-3-memory
python starter.py
```
**What to try:**
```
You: Remember that my name is Alex and I love pizza
You: What's my name?
You: quit
```
**What happens:** Agent remembers your preferences  
**Time:** Interactive (try for 2 minutes)

---

### Challenge 4: Full Agent
```bash
cd April-2026/challenge-4-full-agent
python starter.py
```
**What to try:**
```
You: Remember my name is Sam and I'm from Boston
You: What's the weather in my city and what's 100 * 25?
You: quit
```
**What happens:** Agent uses multiple tools and memory together  
**Time:** Interactive (try for 3 minutes)

---

### Challenge 5: AWS Documentation Expert
```bash
# First install the MCP server
pip install awslabs.aws-documentation-mcp-server

# Then run
cd April-2026/challenge-5-innovate-mcp-chatbot
python starter.py
```
**What to try:**
```
You: What is AWS Lambda?
You: How do I create an S3 bucket?
You: Remember that I'm learning about serverless
You: quit
```
**What happens:** Agent searches real AWS docs and remembers your learning  
**Time:** Interactive (try for 5 minutes)

---

## 🐛 Quick Troubleshooting

### Problem: "Module not found"
```bash
pip install strands-agents strands-tools boto3 faiss-cpu requests
```

### Problem: "AWS credentials not found"
```bash
aws configure
# Enter your credentials
```

### Problem: "Ollama connection refused"
```bash
# In a separate terminal:
ollama serve
```

### Problem: "Amazon Nova Pro access denied"
1. Go to AWS Console → Bedrock
2. Click "Model access"
3. Enable "Amazon Nova Pro"
4. Wait 1 minute for approval

---

## ✅ Verify Everything Works

Run this script to check your setup:
```bash
python verify_setup.py
```

It will tell you exactly what's missing!

---

## 📖 What Each Challenge Teaches

| Challenge | You Learn | Time |
|-----------|-----------|------|
| 1 | Basic agent setup | 5 min |
| 2 | Adding tools | 10 min |
| 3 | Persistent memory | 10 min |
| 4 | Combining features | 15 min |
| 5 | MCP integration | 20 min |

**Total Learning Time:** ~1 hour

---

## 🎯 Recommended Learning Path

### For Beginners:
1. Start with **Challenge 1** (simplest)
2. Move to **Challenge 2** (learn tools)
3. Try **Challenge 3** (add memory)
4. Complete **Challenge 4** (combine everything)
5. Innovate with **Challenge 5** (build something cool)

### For Experienced Developers:
1. Jump to **Challenge 4** (see everything working)
2. Go back to **Challenge 1-3** (understand the pieces)
3. Innovate with **Challenge 5** (build your own)

---

## 💡 Quick Tips

### Tip 1: Start Simple
Don't try to understand everything at once. Run Challenge 1 first!

### Tip 2: Read the Output
The agents print helpful messages showing what they're doing.

### Tip 3: Experiment
Change the questions, modify the prompts, break things and fix them!

### Tip 4: Use the Docs
Each challenge folder has a README.md with detailed explanations.

### Tip 5: Check verify_setup.py
If something doesn't work, run `python verify_setup.py` first.

---

## 🎓 Next Steps After Quick Start

1. **Read SETUP_AND_RUN.md** for detailed explanations
2. **Read individual challenge READMEs** for specific details
3. **Modify the code** to add your own features
4. **Create new tools** for Challenge 4
5. **Build your own MCP agent** for Challenge 5

---

## 🆘 Need Help?

1. **Check verify_setup.py** - Automated diagnostics
2. **Read SETUP_AND_RUN.md** - Detailed troubleshooting
3. **Check individual READMEs** - Challenge-specific help
4. **Review error messages** - They usually tell you what's wrong

---

## 🎉 You're Ready!

Pick a challenge and start coding! 🚀

```bash
# The simplest start:
cd April-2026/challenge-2-tools
python starter.py
```

**Have fun building AI agents!** 🤖

---

## 📋 One-Command Setup (Advanced)

If you want to set up everything at once:

```bash
# Install all dependencies
pip install strands-agents strands-tools boto3 faiss-cpu requests awslabs.aws-documentation-mcp-server

# Configure AWS
aws configure

# Verify setup
python verify_setup.py

# Run your first challenge
cd April-2026/challenge-2-tools && python starter.py
```

---

**Time to complete Quick Start:** 5-10 minutes  
**Time to run all challenges:** 30-60 minutes  
**Time to master AI agents:** Priceless! 🏆
