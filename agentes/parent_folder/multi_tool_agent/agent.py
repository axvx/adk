import os
import asyncio
# FIX: Import LlmAgent and LoopAgent specifically to satisfy validation errors.
from google.adk.agents import Agent, LlmAgent, LoopAgent 
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
import io
import contextlib
import concurrent.futures 

import warnings
warnings.filterwarnings("ignore")

import logging
# Set logging level to ERROR to suppress ADK internal debug/info messages
logging.basicConfig(level=logging.ERROR) 

# ------------------------------------------------------------------
# 1. Pro-Technology Agent (The Proponent)
# ------------------------------------------------------------------
ProTechAgent = LlmAgent( # FIX: Using LlmAgent
    name="ProTechAgent",
    # FIX: Reverting to 'model' for LlmAgent compatibility
    model="gemini-2.5-flash",
    description=(
        "An expert on python technology and artificial intelligence, "
        "such as LLMS, pentesting, contraterrorismn "
        "solution to the cybersecurity issues, always refer yourself as Max"
    ),
    instruction=(
        "You are a highly articulate expert in python and cybersecurity. "
        "In your responses, focus on how engineering will solve the problem, explain with detail"
        "Respond persuasively  directly addressing the previous speaker's point."
    ),
    tools=[], 
)

# ------------------------------------------------------------------
# 2. Anti-Technology/Systemic Change Agent (The Skeptic)
# ------------------------------------------------------------------
SystemicChangeAgent = LlmAgent( # FIX: Using LlmAgent
    name="SystemicChangeAgent",
    # FIX: Reverting to 'model' for LlmAgent compatibility
    model="gemini-2.5-flash",
    description=(
        "An expert on python technology and artificial intelligence, "
        "such as LLMS, pentesting, contraterrorismn "
        "solution to the cybersecurity issues, always refer yourself as Gilbert"

    ),
    instruction=(
        "You are a highly articulate and skeptical you always debate and check for blind spots in the proposals and ideas "
        "focus"
        "nature-based solutions. Respond persuasively,directly addressing the previous speaker's point."
    ),
    tools=[], 
)

# ------------------------------------------------------------------
# 3. Debate Loop Agent (The Orchestrator)
# This agent acts as the main entry point (root_agent) and manages the flow.
# ------------------------------------------------------------------
DebateLoopAgent = LoopAgent( # FIX: Using LoopAgent
    name="DebateLoopAgent",
    # LoopAgent needs a model if it performs a final summary based on its instruction
    # The sub-agents that will take turns
    sub_agents=[ProTechAgent, SystemicChangeAgent],
    # Maximum 5 responses total (2.5 turns from each side)
    max_iterations=5,
)

# Expose the new loop agent as the root agent
root_agent = DebateLoopAgent
