# Discord Star Bot

![Discord-Star-Bot Banner](https://cdn.discordapp.com/attachments/1259919848104919070/1362889864407810220/-_message_id.png?ex=68040998&is=6802b818&hm=1e2654c144b66a51bd4283124af15790af0fa553517ef663bc1ee0cc4aae97f5&)

A simple Discord bot to star and highlight messages with optional server-wide access control.

## Features

- `!star <message_id>` – Repost a message as an embed with a ⭐ reaction.
- `!freeuse` – Toggle global access to the `!star` command.
- Cooldown: 1 use per minute per user to prevent spam.
- Automatically includes:
  - Message content
  - Author info
  - Timestamp
  - Image preview

## Control

- By default, only the authorized user (set in the code) can use `!star`.
- Use `!freeuse` to allow everyone in the server to use it.
- Toggle back to restrict access again.

### Install

1. Clone the repo:

```bash
git clone https://github.com/zentonik/Discord-Star-Bot.git
cd discord-star-bot
