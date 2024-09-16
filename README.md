# AI powered Vacation Rental Review Summarizer.

Delivering a concise, Cliff Notes-style summary of short-term rental reviews for quick and effective insights into guest experiences.

## Features

- Adaptive Responses: Uses conversation history to provide context-aware responses.
- Streamed Responses: Delivers model responses in real-time as they are generated.
- Configurable System Prompts: Allows enabling/disabling of system prompts and vacation rental context.

## Installation and Setup

1. **Clone the Repository**:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

1. **API Keys**:

   - Copy the `.env.sample` file and rename it to `.env`
   - Replace the placeholder values with your actual API keys

2. **System Prompts and STR Context**:

   - Adjust the `ENABLE_SYSTEM_PROMPT` and `ENABLE_STR_CONTEXT` flags as needed.

3. **Customize Prompts**:
   - Modify the prompt templates in the `prompts.py` file to suit your context.

## Running the Application

1. **Activate the Virtual Environment** (if not already activated):

   ```sh
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

2. **Run the Chainlit App**:

   ```sh
   chainlit run app.py -w
   ```

3. Open your browser and navigate to the URL displayed in the terminal.
