# Copyright (c) Microsoft. All rights reserved.

from typing import ClassVar, Final

from agent_framework._pydantic import AFBaseSettings
from pydantic import SecretStr

BEDROCK_DEFAULT_MAX_TOKENS: Final[int] = 8192
BEDROCK_DEFAULT_REGION: Final[str] = "us-east-1"
BEDROCK_DEFAULT_ANTHROPIC_VERSION: Final[str] = "bedrock-2023-05-31"


class BedrockSettings(AFBaseSettings):
    """AWS Bedrock settings.

    The settings are first loaded from environment variables with the prefix 'AWS_BEDROCK_'.
    If the environment variables are not found, the settings can be loaded from a .env file
    with the encoding 'utf-8'. If the settings are not found in the .env file, the settings
    are ignored; however, validation will fail alerting that the settings are missing.

    Keyword Args:
        bearer_token: The AWS bearer token for Bedrock authentication (API key).
        region_name: AWS region name (default: us-east-1).
        chat_model_id: The Bedrock model ID to use.
        access_key_id: AWS access key ID for standard authentication.
        secret_access_key: AWS secret access key for standard authentication.
        session_token: AWS session token for temporary credentials.
        anthropic_api_version: Anthropic API version for Claude models (default: bedrock-2023-05-31).
        use_converse_api: Whether to use Converse API (default: True).
        default_max_tokens: Default maximum tokens for completions (default: 8192).
            Note: This is a fallback value. Different models support different limits:
            - Claude 3.5 Sonnet v2: 8,192 tokens
            - Claude 3.7 Sonnet: up to 128K tokens (with beta header)
            - Claude 4.5 Sonnet: up to 64K tokens
            Override per-request via ChatOptions(max_tokens=...) for higher limits.
        env_file_path: If provided, the .env settings are read from this file path location.
        env_file_encoding: The encoding of the .env file, defaults to 'utf-8'.

    Examples:
        .. code-block:: python

            from agent_framework_bedrock import BedrockSettings

            # Using environment variables
            # Set AWS_BEDROCK_BEARER_TOKEN=your_bearer_token
            # AWS_BEDROCK_REGION_NAME=us-east-1
            # AWS_BEDROCK_CHAT_MODEL_ID=us.anthropic.claude-3-5-sonnet-20241022-v2:0

            # Or passing parameters directly
            settings = BedrockSettings(
                bearer_token="your_bearer_token",
                chat_model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0"
            )

            # Or loading from a .env file
            settings = BedrockSettings(env_file_path="path/to/.env")
    """

    env_prefix: ClassVar[str] = "AWS_BEDROCK_"

    # Authentication credentials
    bearer_token: SecretStr | None = None
    access_key_id: SecretStr | None = None
    secret_access_key: SecretStr | None = None
    session_token: SecretStr | None = None

    # Configuration
    region_name: str = BEDROCK_DEFAULT_REGION
    chat_model_id: str | None = None

    # Additional options
    anthropic_api_version: str = BEDROCK_DEFAULT_ANTHROPIC_VERSION
    use_converse_api: bool = True
    default_max_tokens: int = BEDROCK_DEFAULT_MAX_TOKENS
