# Urban Court Menu — Setup Guide
## Antigravity + Claude Code

---

## What You're Looking At

In your screenshot you have two AI panels open:
- **Claude Code tab** (main editor, centre) — this is what you use for this project
- **Antigravity / Gemini panel** (right sidebar) — ignore this for now

All your prompts go into the **Claude Code input box** at the bottom of the centre panel ("Ask Claude to edit...").

---

## Step 1 — Set Up Your Project Folder

1. Download and unzip `urbancourt_project.zip` to somewhere clean on your computer
   - Suggested path: `C:\Projects\urbancourt\` or `~/Projects/urbancourt/`
   - After unzipping you should have a folder containing:
     ```
     urbancourt_project/
     ├── CONTEXT.md
     ├── PROMPTS.md
     ├── QUICK_REFERENCE.md
     ├── urbancourt_menu_v2.html
     └── vip_menu_final.html
     ```

2. In Antigravity, click **"Open Folder"** (the blue button in the Explorer panel on the left)

3. Navigate to and select the `urbancourt_project` folder

4. Antigravity will reload with the folder open. You'll see all the files in the left panel.

---

## Step 2 — Open Claude Code

1. Click the **Claude Code tab** at the top of the editor (the one with the ✳ asterisk icon)
   - If it's not open: go to the top menu → **View** → **Claude Code** (or press the shortcut shown)

2. You should see the Claude Code interface with "Ask Claude to edit..." at the bottom

3. Make sure the input is in **Agent mode** (you'll see "Ask before edits" toggle at the bottom right — this is fine to leave on for now)

---

## Step 3 — First Message (Prompt 0)

Copy and paste this **exactly** into the Claude Code input box and press Enter (or the orange arrow button):

```
Read the file CONTEXT.md in this project carefully — it contains the complete brief for the Urban Court digital menu project.

Then open urbancourt_menu_v2.html and confirm you can see the current state of the menu.

Also open vip_menu_final.html — this is the design reference (the Super VIP drinks menu). Study its CSS carefully — specifically the colour variables, typography, card hover effects, and how the bottle images are masked into the black background using mask-image with radial gradients.

Once you have read both files, give me a summary of:
1. What the current menu looks like and what it contains
2. What design techniques from the VIP menu we need to replicate/extend
3. What you think the highest priority next step is

Do not make any changes yet. Just read and report back.
```

---

## Step 4 — Claude Code Will Read Your Files

Claude Code will:
- Read CONTEXT.md (the full project brief)
- Open and analyse both HTML files
- Give you a summary and recommendations

**This is important** — Claude Code has full access to your files in the folder. Unlike the chat window, it can read, edit, write, and create files directly. When it suggests a change, you'll see a diff (before/after) that you approve before it's applied.

---

## Step 5 — How to Use Claude Code Day-to-Day

### Asking for changes
Just describe what you want in plain language. Examples:
- *"Make the hero section taller and add a subtle parallax scroll effect"*
- *"Add a 'Currently unavailable' state to the Oshee Lemon card"*
- *"The Russian translation for the smoothie base label is wrong — fix it"*

### Using the prepared prompts
Open `PROMPTS.md` in the editor. Copy any of the 10 prompts and paste into Claude Code's input. They're written to work exactly in this environment.

### Previewing your work
- In Antigravity, right-click `urbancourt_menu_v2.html` in the Explorer panel
- Select **"Open with Live Server"** (if you have the Live Server extension) or
- Simply open the file in Chrome: **File → Open File** in Chrome → navigate to the file

### When Claude Code makes edits
- It shows you a diff — green lines are additions, red are removals
- Click **Accept** to apply, or **Reject** to undo
- If you have "Ask before edits" enabled, it'll ask you before touching files

---

## Step 6 — Recommended First Session Workflow

After Prompt 0, follow up with these in order:

**Message 2:**
```
Now I want to refine the smoothie base selector. Open urbancourt_menu_v2.html and:

1. When a base pill is selected, add a soft gold glow pulse animation (not just a border colour change)
2. Add a small confirmation line below the selector that appears after selection: "Your [smoothie name] will be prepared with [selected base]" — in italic, very small, gold-dim colour
3. Make the confirmation line also work in Russian when the language is set to RU
4. Make sure selecting a new option replaces the previous confirmation line, not adds another one

Show me the diff before applying.
```

**Message 3:**
```
Now look at PROMPTS.md — specifically Prompt 7 (animated section transitions). Implement that now. Show me the diff before applying.
```

---

## Useful Antigravity Shortcuts

| Action | Shortcut |
|---|---|
| Open file | `Ctrl + P` → type filename |
| Open terminal | `` Ctrl + ` `` |
| Split editor | `Ctrl + \` |
| Toggle sidebar | `Ctrl + B` |
| Format document | `Shift + Alt + F` |
| Find in files | `Ctrl + Shift + F` |

---

## Tips for Working in Claude Code

- **Be specific** — "make the card border glow gold on hover" is better than "make cards look better"
- **Reference files by name** — "in urbancourt_menu_v2.html, find the `.base-selector` class..."
- **Ask it to explain** — "explain what changes you made and why" after each edit
- **Use @ mentions** — type `@urbancourt_menu_v2.html` to attach the file directly to your message
- **Undo is safe** — if you don't like a change, just ask "undo that last change" or use Ctrl+Z

---

## If Something Goes Wrong

- **File got corrupted**: The original is safe in the zip — re-extract and start again
- **Claude Code seems confused**: Start a new conversation in the Claude Code tab (click the + or history icon)
- **Changes applied you didn't want**: `Ctrl+Z` in the file, or ask "revert to the previous version of this file"
- **Can't see your file changes**: Make sure you're looking at the saved file in Chrome, not a cached version — do a hard refresh (Ctrl+Shift+R)
