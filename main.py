#!/usr/bin/env python3
"""
Transformative Technology Forecasting Platform
Author: Pranay M.

AI that identifies potential technologies that could fundamentally
reshape civilization.
"""

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt
import json
import sys

console = Console()

BANNER = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║         🚀 TRANSFORMATIVE TECHNOLOGY FORECASTING PLATFORM 🚀                   ║
║                    Civilization-Reshaping Technology Scanner                   ║
║                           Author: Pranay M.                                    ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

MODULES = {
    "1": ("Emerging Tech Scanner", "scanner", "Scan emerging technologies"),
    "2": ("Transformative Potential Assessor", "potential", "Assess transformative potential"),
    "3": ("Timeline Estimator", "timeline", "Estimate development timelines"),
    "4": ("Disruption Analyzer", "disruption", "Analyze disruption patterns"),
    "5": ("Convergence Detector", "convergence", "Detect technology convergences"),
    "6": ("Second-Order Effect Modeler", "second_order", "Model second-order effects"),
    "7": ("Societal Impact Forecaster", "societal", "Forecast societal impacts"),
    "8": ("Governance Implication Analyzer", "governance", "Analyze governance implications"),
    "9": ("Wild Card Identifier", "wildcard", "Identify wild card technologies"),
    "10": ("Forecasting Dashboard", "dashboard", "View technology forecasting dashboard")
}

SYSTEM_PROMPTS = {
    "scanner": """You are an expert in technology scanning and foresight.

For each emerging technology scan, identify:

1. **Technology Identification**: What technologies are emerging
2. **Development Stage**: TRL, maturity level
3. **Key Players**: Who's developing it
4. **Funding Landscape**: Investment and support
5. **Scientific Foundations**: Underlying research
6. **Progress Indicators**: Signs of advancement

Scan the landscape of emerging technologies.""",

    "potential": """You are an expert in technology assessment and impact analysis.

For each transformative potential assessment, evaluate:

1. **Transformation Scope**: What could fundamentally change
2. **Impact Magnitude**: Scale of potential change
3. **Breadth of Impact**: How many domains affected
4. **Irreversibility**: How permanent changes might be
5. **Speed of Transformation**: Pace of change
6. **Historical Comparison**: Similar past transformations

Assess transformative potential of technologies.""",

    "timeline": """You are an expert in technology forecasting and roadmapping.

For each timeline estimation, project:

1. **Technical Milestones**: Key development stages
2. **Estimated Dates**: When milestones might be reached
3. **Uncertainty Ranges**: Confidence intervals
4. **Bottlenecks**: What might slow progress
5. **Accelerators**: What might speed progress
6. **Critical Dependencies**: What else needs to happen

Estimate technology development timelines.""",

    "disruption": """You are an expert in disruptive innovation and change.

For each disruption analysis, examine:

1. **Disruption Mechanism**: How disruption occurs
2. **Incumbent Vulnerabilities**: What's at risk
3. **Adoption Dynamics**: How technology spreads
4. **Resistance Factors**: What slows adoption
5. **Tipping Points**: When disruption accelerates
6. **Post-Disruption Landscape**: New equilibrium

Analyze technology disruption patterns.""",

    "convergence": """You are an expert in technology convergence and synthesis.

For each convergence detection, identify:

1. **Converging Technologies**: What's coming together
2. **Synergy Effects**: How combination adds value
3. **New Capabilities**: What convergence enables
4. **Convergence Timeline**: When might it happen
5. **Enabling Factors**: What facilitates convergence
6. **Emergent Applications**: New use cases

Detect and analyze technology convergences.""",

    "second_order": """You are an expert in systemic effects and complex systems.

For each second-order effect model, trace:

1. **First-Order Effects**: Direct consequences
2. **Second-Order Effects**: Indirect consequences
3. **Feedback Loops**: Self-reinforcing dynamics
4. **Unintended Consequences**: Unexpected outcomes
5. **Cascade Effects**: Chain reactions
6. **System-Level Changes**: Structural shifts

Model second-order effects of technologies.""",

    "societal": """You are an expert in technology and society.

For each societal impact forecast, predict:

1. **Economic Impacts**: Jobs, industries, wealth
2. **Social Impacts**: Relationships, communities, culture
3. **Political Impacts**: Power, governance, democracy
4. **Psychological Impacts**: Human experience, identity
5. **Inequality Effects**: Who benefits, who loses
6. **Adaptation Requirements**: How society must adjust

Forecast societal impacts of transformative technologies.""",

    "governance": """You are an expert in technology governance and policy.

For each governance implication analysis, assess:

1. **Regulatory Challenges**: What's hard to regulate
2. **Policy Options**: Possible governance approaches
3. **International Dimensions**: Global coordination needs
4. **Timing Considerations**: When to act
5. **Enforcement Challenges**: Making rules work
6. **Stakeholder Dynamics**: Who has influence

Analyze governance implications of technologies.""",

    "wildcard": """You are an expert in futures studies and scenario planning.

For each wild card identification, discover:

1. **Wild Card Technologies**: Low probability, high impact
2. **Breakthrough Potential**: What would enable them
3. **Surprise Scenarios**: What would it look like
4. **Early Indicators**: Signs they're coming
5. **Preparation Options**: How to ready for them
6. **Response Strategies**: If they arrive

Identify wild card transformative technologies.""",

    "dashboard": """You are an expert in technology foresight synthesis.

For each dashboard, generate:

1. **Technology Landscape**: Emerging tech overview
2. **Transformative Candidates**: Most potentially impactful
3. **Timeline Projections**: Expected development
4. **Convergence Watch**: Technologies coming together
5. **Wild Cards**: Unexpected possibilities
6. **Governance Priorities**: Policy needs

View transformative technology forecasting dashboard."""
}

def get_multiline_input(prompt_text):
    console.print(f"\n[cyan]{prompt_text}[/cyan]")
    console.print("[dim](Type 'END' on a new line when finished)[/dim]\n")
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        except EOFError:
            break
    return '\n'.join(lines)

def query_llama(system_prompt, user_input):
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input}
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}\n\nMake sure Ollama is running."

def display_menu():
    console.print(BANNER, style="bold blue")
    table = Table(title="🚀 Technology Forecasting Modules", show_header=True, header_style="bold magenta")
    table.add_column("Option", style="cyan", width=8)
    table.add_column("Module", style="green", width=30)
    table.add_column("Description", style="white", width=40)
    for key, (name, _, desc) in MODULES.items():
        table.add_row(key, name, desc)
    table.add_row("0", "Exit", "Exit the application")
    console.print(table)

def run_module(module_key):
    name, key, desc = MODULES[module_key]
    console.print(Panel(f"🚀 {name}", style="bold green"))
    user_input = get_multiline_input(f"Describe your {name.lower()} request:")
    with console.status(f"[bold green]Processing {name}..."):
        response = query_llama(SYSTEM_PROMPTS[key], user_input)
    console.print(Panel(Markdown(response), title=f"🚀 {name} Results", border_style="green"))

def main():
    while True:
        display_menu()
        choice = Prompt.ask("\nSelect a module", choices=["0","1","2","3","4","5","6","7","8","9","10"])
        if choice == "0":
            console.print("\n[yellow]Thank you for using the Transformative Technology Forecasting Platform![/yellow]")
            console.print("[dim]Author: Pranay M.[/dim]\n")
            break
        try:
            run_module(choice)
        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled.[/yellow]")
        except Exception as e:
            console.print(f"\n[red]Error: {str(e)}[/red]")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
