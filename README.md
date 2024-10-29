# Franchise Research Assistant

A CrewAI-based research assistant specialized in franchise investment analysis, powered by [crewAI](https://crewai.com).

## Features

- Comprehensive franchise research and analysis
- Investment strategy recommendations
- Market analysis and competitor research
- Automated report generation
- Customizable research parameters

## Prerequisites

- Python >=3.10,<3.13
- Poetry (for dependency management)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd franchise-research-assistant
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Set up your environment variables:
```bash
cp .env.example .env
```
Then edit `.env` with your API keys:
- `OPENAI_API_KEY` - Your OpenAI API key
- `SERPER_API_KEY` - Your Serper.dev API key

## Usage

Run the research assistant:
```bash
poetry run research
```

Additional commands:
```bash
# Train the crew
poetry run train-crew <iterations> <filename>

# Replay a specific task
poetry run replay-crew <task_id>

# Run tests
poetry run test-crew <iterations> <model_name>
```

## Configuration

- `src/crewai_research_assistant/config/agents.yaml` - Define agent roles and capabilities
- `src/crewai_research_assistant/config/tasks.yaml` - Configure research tasks and workflows
- `src/crewai_research_assistant/crew.py` - Customize crew logic and tool integration
- `src/crewai_research_assistant/main.py` - Modify input parameters and execution flow

## Project Structure

```
├── src/
│   └── crewai_research_assistant/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── tools/
│       │   └── custom_tool.py
│       ├── crew.py
│       └── main.py
├── reports/
├── tests/
├── .env.example
├── pyproject.toml
└── README.md
```

## Development

```bash
# Install dev dependencies
poetry install --with dev

# Run tests
poetry run pytest

# Format code
poetry run black .
poetry run isort .

# Type checking
poetry run mypy .
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, questions, or feedback:
- Visit [crewAI documentation](https://docs.crewai.com)
- [Join crewAI Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with crewAI docs](https://chatg.pt/DWjSBZn)
