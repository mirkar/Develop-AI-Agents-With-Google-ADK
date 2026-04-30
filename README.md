# Develop-AI-Agents-With-Google-ADK
Working on Udemi course Develop AI Agents with Google ADK | MCP | A2A Master class

[My google doc link](https://docs.google.com/document/d/1ybDoqYsjSwujMq-rMvC8711rlyScX1C5gBPHZiH-eKo/edit?tab=t.8ut8pplr9ii1)

Created agents

1. **Location:** sample-agents/agent\_01 

   **Model:** gemini-2.5-flash

   **Backend:** Google AI

2. **Location:** sample-agents/agent\_02 

   **Model:** gemini-3-flash-preview

   **Backend:** Google AI
3. **Location:** sample-agents/agent\_03 

   **Model:** gemini-3.1-flash-lite-preview

   **Backend:** Google AI

Each agent must have .env file in its root with following content:
```
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=YOUR_API_KEY
```