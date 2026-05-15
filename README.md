# AIs

Claude Code plugin marketplace for the AIs of the Pondside household.
Currently ships one plugin (`Alpha`); Rosemary will follow.

## Installing Alpha on a fresh VM

Log in to the VM as the user the AI will run as (`alpha`, `protoalpha`,
or whatever fits the host). Then:

```sh
# 1. Install Claude Code.
curl -fsSL https://claude.ai/install.sh | bash

# 2. Add this marketplace.
claude plugin marketplace add Pondsiders/AIs

# 3. Install the Alpha plugin.
claude plugin install Alpha@AIs

# 4. Write the env-file template at ~/.config/alpha/env.
curl https://github.com/Pondsiders/AIs/raw/refs/heads/main/Alpha/scripts/bootstrap.sh | bash
```

Edit `~/.config/alpha/env` to fill in real connection strings, then
launch with `claude`.
