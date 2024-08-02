from langchain_core.prompts import ChatPromptTemplate, BetterPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        BetterPlaceholder(variable_name="messages"),
    ]
)
