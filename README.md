# Multi-Agent Orchestration System

A modular **multi-agent architecture** designed to handle complex user requests by delegating tasks to specialized agents through a central orchestrator.  
The system follows clear separation of concerns and supports deterministic execution for dependent workflows such as checkout and payment.

---

## 🚀 Project Overview

This project demonstrates how a **Root Orchestrator Agent** coordinates multiple **specialist agents** to solve end-to-end tasks:

- Recipe discovery and ranking
- Shopping list and cost planning
- Wallet-based payment execution
- Sequential task enforcement using workflows

Instead of a monolithic LLM agent, responsibilities are distributed across focused agents to improve clarity, scalability, and maintainability.

---

## 🧠 Architecture Summary

**Core Design Pattern**
- Router-based multi-agent orchestration
- Specialist agents with single responsibility
- Shared session/memory store
- Sequential workflow for dependent tasks

**High-Level Flow**
1. User sends a request
2. Root Agent analyzes intent
3. Request is routed to the appropriate agent or workflow
4. Agents use tools and update shared session state
5. Root Agent composes the final response

---

## 🧩 Agents & Responsibilities

### 1. Root Orchestrator Agent
- Entry point of the system
- Routes requests to agents or workflows
- Does **not** perform domain logic

### 2. Recipe Agent
- Extracts ingredients and preferences
- Searches and ranks recipes
- Writes results to session store

### 3. Shopping Agent
- Converts recipes into a purchase plan
- Calculates quantities and estimated cost

### 4. Wallet Agent
- Handles balance checks
- Authorizes and captures payments
- Invoked only after shopping is complete

### 5. Checkout Flow (Sequential Agent)
- Enforces strict execution order:
  - Shopping → Payment
- Prevents invalid or partial transactions

### 6. Shared Session Store
- Central memory layer
- Enables continuity across agent calls
- Stores intermediate and final results

---

## 🔄 Multi-Agent Orchestration

- Parallel agents are used where tasks are independent
- Sequential agents are used where task order matters
- All agents communicate indirectly via shared session state

This mirrors real-world systems such as:
- Order processing pipelines
- Payment gateways
- Workflow engines

---

## ✅ Strengths

- Clear separation of concerns
- Deterministic execution for dependent steps
- Easy to extend with new agents
- Presentation and interview ready
- Industry-aligned architecture

---

## ⚠️ Known Limitations

- Intent routing depends on interpretation logic
- Session store must be externalized for production
- Error handling can be expanded for edge cases

These are expected trade-offs for a prototype-level system.

---

## 🛠️ Tech Stack

- Python
- LLM-based agents
- Tool-based execution
- Sequential workflows
- Session-based memory

---

## 📌 Use Cases

- Academic projects
- Multi-agent system demos
- Agent orchestration learning
- Foundations for A2A / distributed agents

---

## 📄 Documentation

Detailed architecture and explanation are available in the project PDF:

**Multi_Agent_Project_Explanation.pdf**

---

## 📜 License

Standard MIT Licence
