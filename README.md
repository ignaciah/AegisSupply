
   [ Email/ERP Trigger ] 
             │
             ▼
   ┌────────────────────────────────┐
   │      UiPath Agent Builder      │ <─── [ Context Grounding: Vendor PDFs ]
   │    (LLM Reasoning Engine)     │
   └────────────────────────────────┘
             │
      ┌──────┴──────┐
      ▼             ▼
  [Tool 1: ERP]  [Tool 2: Alternate Vendor API] ──► [Human-in-the-Loop Validation]


AegisSupply 🛡️
### Autonomous Supply Chain Exception Handler & Vendor Negotiator
**Built for the UiPath AgentHack 2026**

AegisSupply is an intelligent, agentic automation solution designed to mitigate supply chain disruptions. Instead of relying on static, linear RPA paths, AegisSupply leverages **UiPath Agent Builder**, **UiPath Integration Service**, and **Context Grounding (RAG)** to dynamically reason through vendor delays, cross-reference historical contracts, search external marketplaces for alternatives, and autonomously negotiate resolutions.

---

## 🚀 Key Features

* **Agentic Reasoning Engine:** Powered by UiPath Agent Builder to dynamically determine the best course of action based on incoming delay alerts.
* **Context Grounding (RAG):** Ingests historical Vendor Master Service Agreements (MSAs) to instantly extract late-delivery penalty clauses.
* **Dynamic Tool Execution:** Connects natively to internal ERPs (via UiPath Integration Service) and external supplier APIs.
* **Human-in-the-Loop (HITL):** Errant costs or major shifts are automatically routed to a supervisor via UiPath Action Center before any communications are dispatched.

---

## 🏗️ Architecture & Workflow

1. **Trigger:** An incoming shipment delay email or ERP alert is intercepted.
2. **Analysis:** The AegisSupply Agent analyzes the impact and invokes the `Get_PO_Details` tool.
3. **Contract Auditing:** The Agent queries its grounded knowledge base (Vendor Contracts) to check for legal leverage (e.g., 5% discount per week delayed).
4. **Alternative Sourcing:** If critical, the Agent calls `Search_Marketplace_API` to source alternative vendors.
5. **Human Validation:** If the financial impact exceeds a $500 threshold, a UiPath Form Task is generated for human approval.
6. **Resolution:** A professionally tailored, legally backed negotiation email is drafted and sent to the defaulting vendor.

---

## 📁 Repository Structure

* `/workflows` : Exported UiPath Studio Web project files (`.zip`).
* `/prompts` : System instructions, agent behavioral guardrails, and tool schemas.
* `/context-documents` : Dummy vendor MSAs and contracts used for RAG grounding.
* `/mock-api` : Simple JSON payloads simulating the live marketplace API responses.

---

## 🛠️ Setup & Installation

1. **UiPath Studio Web:** Import the workflows located in the `/workflows` directory.
2. **Agent Builder:** Create a new Agent in the UiPath Automation Cloud, paste the prompt from `/prompts/system_prompt.txt`, and link the imported workflows as tools.
3. **Storage Buckets:** Upload the PDFs in `/context-documents` to a UiPath Storage Bucket and link it to the Agent's Context tab.
4. **Run:** Trigger the automation
