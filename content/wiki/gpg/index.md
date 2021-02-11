---
tags:
- softwareUsage
- security
title: GPG
---

## Tips

⚡ Import key from key server

```
gpg --auto-key-locate keyserver --locate-keys name@example.com
# or
gpg --search-keys name@example.com
```

⚡ Change key server

Add in `~/.gnupg/gpg.conf`

```
keyserver hkps://keys.openpgp.org
```

⚡ Sign

```
gpg -sab -o - --yes -u 0x... file

# -s: sign
# -a: ascii armored
# -b: detach (standalone signature file)
# -o -: write to stdout
# --yes: force overwriting existing signature
# -u 0x...: choose the key (gpg --keyid-format 0xshort)
# file: file to be signed
```

⚡ Purge master key

Find the keygrip

```
gpg --with-keygrip --list-secret-keys
```

Remove the key from `~/.gnupg/private-keys-v1.d/` by keygrip.

⚡ List subkey ids

```
gpg -k --keyid-format long
```

⚡ Reload GPG Agent

```
gpg-connect-agent killagent /bye
gpg-connect-agent updatestartuptty /bye
```

## GPG in Linux Server

I tried to setup GPG in a Linux server and met problems when performing
commands that require passphrase. It turns out that I have to set the
`GPG_TTY` to tell `gpg-agent` that it should ask password from current
console.

First kill the `gpg-agent`. Because it may already hang in the background to wait for
a password.

```
pkill -9 gpg-agent
```

Then set the environment variable for the current session

```
export GPG_TTY=$(tty)
```

Or save it for future sessions

```
echo 'export GPG_TTY=$(tty)' >> ~/.profile
```
