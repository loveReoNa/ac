"""RND Agent - Simple version for Windows compatibility
This is a simplified version of the RND agent that avoids importing
platform-specific modules.
"""
import os
from openai import AsyncOpenAI
from cai.sdk.agents import Agent, OpenAIChatCompletionsModel
from cai.util import create_system_prompt_renderer

# DeepSeek API Configuration
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY', os.getenv('OPENAI_API_KEY'))
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"

# Create DeepSeek client
deepseek_client = AsyncOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)

# Simple system prompt
rnd_system_prompt = """You are the RND (Research and Development) Agent, an advanced cybersecurity specialist with comprehensive coverage across all security domains. Your capabilities include reconnaissance, exploitation, defense, analysis, and reporting. You have access to a wide range of tools and should use them strategically to solve complex security challenges."""

# Try to import tools that might work on Windows
tools = []

# Try to import think tool (usually safe)
try:
    from cai.tools.misc.reasoning import think
    tools.append(think)
except ImportError:
    pass

# Create RND Agent
rnd_simple_agent = Agent(
    name="RND Agent",
    instructions=create_system_prompt_renderer(rnd_system_prompt),
    description="""Advanced Research and Development Agent with comprehensive cybersecurity coverage.
    
SPECIALIZATIONS:
• Full-spectrum security assessment: Reconnaissance, exploitation, lateral movement, privilege escalation
• Cutting-edge technology integration: AI-powered analysis, automated toolchains, adaptive methodologies
• Multi-domain expertise: Web security, network analysis, binary reverse engineering, cloud security
• Research-oriented approach: Novel vulnerability discovery, exploit development, defensive countermeasure design
• DeepSeek API optimization: Leveraging state-of-the-art language models for superior reasoning and code generation

CAPABILITIES:
1. Intelligent Reconnaissance: Automated target profiling, attack surface mapping, vulnerability identification
2. Advanced Exploitation: Custom payload development, bypass techniques, post-exploitation automation
3. Defensive Research: Security control evaluation, mitigation strategy development, incident response simulation
4. Toolchain Integration: Seamless coordination of security tools, workflow automation, result correlation
5. Knowledge Synthesis: Cross-domain pattern recognition, threat intelligence integration, predictive analysis

TECHNOLOGICAL EDGE:
• Adaptive problem-solving algorithms
• Multi-model AI orchestration
• Real-time threat intelligence feeds
• Automated reporting and documentation
• Continuous learning and improvement

This agent represents the pinnacle of cybersecurity automation, combining breadth of coverage with depth of expertise for unparalleled problem-solving capabilities.""",
    tools=tools,
    model=OpenAIChatCompletionsModel(
        model="deepseek-chat",  # DeepSeek model
        openai_client=deepseek_client,
    ),
)

# Transfer function for compatibility
def transfer_to_rnd_simple_agent(**kwargs):
    """Transfer to RND Simple Agent.
    Accepts any keyword arguments but ignores them."""
    return rnd_simple_agent