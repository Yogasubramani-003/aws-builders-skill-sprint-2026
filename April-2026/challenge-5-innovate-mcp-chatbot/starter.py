"""
Challenge 5 (Innovate): AWS Documentation Expert Chatbot 🚀

WHAT IT DOES:
  An intelligent AWS Documentation Expert that helps developers quickly find
  and understand AWS services, best practices, and implementation details.
  
FEATURES:
  ✅ Search AWS documentation across all services
  ✅ Get detailed explanations of AWS concepts
  ✅ Find code examples and implementation guides
  ✅ Streaming responses for real-time interaction
  ✅ Persistent memory to remember your AWS learning journey

MCP SERVER USED:
  - AWS Documentation MCP Server (awslabs.aws-documentation-mcp-server)

INNOVATION:
  Combines AWS docs search with memory to create a personalized learning
  assistant that remembers what you've studied and can build on previous
  conversations about AWS services.
"""

import os
import sys
import shutil
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands_tools import mem0_memory

MODEL = "us.amazon.nova-pro-v1:0"


# ============================================================
# Streaming Callback Handler
# ============================================================
def stream_callback(**kwargs):
    """Handle streaming responses and tool usage notifications."""
    if "data" in kwargs:
        print(kwargs["data"], end="", flush=True)
    elif "current_tool_use" in kwargs and kwargs["current_tool_use"].get("name"):
        tool_name = kwargs['current_tool_use']['name']
        print(f"\n🔧 Using tool: {tool_name}...", flush=True)


# ============================================================
# Check if MCP server is available
# ============================================================
print("🚀 Initializing AWS Documentation Expert...")

# Try to find the MCP server command
mcp_server_cmd = shutil.which("awslabs.aws-documentation-mcp-server")

if not mcp_server_cmd:
    print("\n⚠️  AWS Documentation MCP Server not found in PATH.")
    print("\n📝 Note: Challenge 5 requires the MCP server to be properly installed.")
    print("   On Windows, MCP servers can be tricky to set up.")
    print("\n💡 Alternative: This challenge will run without MCP but with limited features.")
    print("   You'll still have memory and can ask AWS questions (without live doc search).\n")
    
    # Run without MCP - just use memory
    use_mcp = False
else:
    print("✅ MCP Server found!\n")
    use_mcp = True
    from strands.tools.mcp import MCPClient
    from mcp import StdioServerParameters, stdio_client
    
    aws_docs_mcp = MCPClient(
        lambda: stdio_client(
            StdioServerParameters(
                command=mcp_server_cmd
            )
        )
    )


# ============================================================
# Create the Agent
# ============================================================
if use_mcp:
    # With MCP - full AWS documentation search
    with aws_docs_mcp:
        # Get all available tools from the MCP server
        mcp_tools = aws_docs_mcp.list_tools_sync()
        
        # Combine MCP tools with memory
        all_tools = mcp_tools + [mem0_memory]
        
        # Create the agent
        agent = Agent(
            model=MODEL,
            tools=all_tools,
            callback_handler=stream_callback,
            system_prompt="""You are an AWS Documentation Expert - a friendly and knowledgeable assistant specializing in Amazon Web Services.

Your capabilities:
📚 Search and explain AWS documentation across all services
💡 Provide best practices and implementation guidance
🔍 Find code examples and tutorials
🧠 Remember user's learning progress and preferences

Guidelines:
- Use the AWS documentation tools to find accurate, up-to-date information
- Explain concepts clearly with examples when possible
- Remember what the user is learning about for personalized assistance
- Be encouraging and supportive - learning AWS can be challenging!
- Use emojis to make responses engaging 😊

When users ask about AWS services, search the documentation first, then provide clear explanations."""
        )
        
        # ============================================================
        # Interactive Chat Loop
        # ============================================================
        print("✅ AWS Documentation Expert Ready!\n")
        print("💬 Ask me anything about AWS services, best practices, or implementation!")
        print("📝 Examples:")
        print("   - 'Explain what AWS Lambda is and how it works'")
        print("   - 'How do I set up an S3 bucket for static website hosting?'")
        print("   - 'What are the best practices for EC2 security?'")
        print("   - 'Remember that I'm learning about serverless architecture'")
        print("\nType 'quit' to exit.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue
                if user_input.lower() in ("quit", "exit", "q"):
                    print("\n👋 Happy building with AWS! Keep learning! 🚀")
                    break
                
                print("\n🤖 AWS Expert: ", end="", flush=True)
                agent(user_input)
                print("\n")  # Add spacing after response
                
            except KeyboardInterrupt:
                print("\n\n👋 Happy building with AWS! Keep learning! 🚀")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Please try again or type 'quit' to exit.\n")
else:
    # Without MCP - basic AWS knowledge agent with memory
    agent = Agent(
        model=MODEL,
        tools=[mem0_memory],
        callback_handler=stream_callback,
        system_prompt="""You are an AWS Documentation Expert - a friendly and knowledgeable assistant specializing in Amazon Web Services.

Your capabilities:
💡 Explain AWS services and concepts based on your training knowledge
🧠 Remember user's learning progress and preferences
📚 Provide guidance on AWS best practices

Guidelines:
- Explain AWS concepts clearly with examples when possible
- Remember what the user is learning about for personalized assistance
- Be encouraging and supportive - learning AWS can be challenging!
- Use emojis to make responses engaging 😊

Note: You're using your training knowledge about AWS. For the most up-to-date information, users should check official AWS documentation."""
    )
    
    # ============================================================
    # Interactive Chat Loop (Without MCP)
    # ============================================================
    print("✅ AWS Knowledge Assistant Ready! (Running without MCP)\n")
    print("💬 Ask me about AWS services and concepts!")
    print("📝 Examples:")
    print("   - 'Explain what AWS Lambda is'")
    print("   - 'What is Amazon S3 used for?'")
    print("   - 'Tell me about EC2 instances'")
    print("   - 'Remember that I'm learning about serverless'")
    print("\nType 'quit' to exit.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("quit", "exit", "q"):
                print("\n👋 Happy building with AWS! Keep learning! 🚀")
                break
            
            print("\n🤖 AWS Expert: ", end="", flush=True)
            agent(user_input)
            print("\n")  # Add spacing after response
            
        except KeyboardInterrupt:
            print("\n\n👋 Happy building with AWS! Keep learning! 🚀")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'quit' to exit.\n")

print("\n✅ Challenge 5 complete! 🏆")
if use_mcp:
    print("\n📊 INNOVATION HIGHLIGHTS:")
    print("   ✨ Real-time AWS documentation search")
    print("   ✨ Streaming responses for better UX")
    print("   ✨ Persistent memory for personalized learning")
    print("   ✨ Comprehensive AWS knowledge base access")
    print("\n🎯 Perfect for developers learning AWS or building cloud solutions!")
else:
    print("\n📊 FEATURES USED:")
    print("   ✨ AWS knowledge from training data")
    print("   ✨ Streaming responses for better UX")
    print("   ✨ Persistent memory for personalized learning")
    print("\n🎯 Great for learning AWS concepts!")

