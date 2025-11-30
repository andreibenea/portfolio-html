// games/c-eleven/main.js

const outputEl = document.getElementById("output");
const formEl = document.getElementById("command-form");
const inputEl = document.getElementById("input");
const statusEl = document.getElementById("status");
const submitBtn = formEl.querySelector('button[type="submit"]');


let pyodideReadyPromise = null;
let gameOver = false;

// From the HTML page location (pages/projects/...), this resolves to /games/c-eleven/py/
const PY_ROOT = "../../games/c-eleven/py";

// List all Python files needed by the game
const PY_FILES = [
  "world.py",
  "handler.py",
  "npc.py",
  "game.py",
  "player.py",
  "event_emitter.py",
  "commands.py",
  "web_main.py",
  "scenes/__init__.py",
  "scenes/c11.py",
  "scenes/data_core.py",
  "scenes/engineering_bay.py",
  "scenes/hallway_ground.py",
  "scenes/hallway_upper.py",
  "scenes/j23.py",
  "scenes/maintenance_tunnels.py",
  "scenes/med_bay.py",
  "scenes/overseer_office.py",
  "scenes/reactor_catwalk.py",
  "scenes/security_office.py",
  "scenes/under_construction.py",
  "scenes/vault_door_room.py",
  "dialogues/__init__.py",
  "dialogues/intercom_c11.py",
  "dialogues/juno_j23.py",
  "dialogues/juno_j23_2.py",
  "dialogues/juno_j23_3.py",
  "dialogues/riley_med_bay.py",
  "dialogues/riley_med_bay_2.py",
  "dialogues/riley_med_bay_3.py",
  "dialogues/warden_data_core.py",
  "dialogues/warden_data_core_2.py",
];

function appendLine(text, kind = "narration") {
  const div = document.createElement("div");
  div.className = `line ${kind}`;
  div.textContent = text;
  outputEl.appendChild(div);
  outputEl.scrollTop = outputEl.scrollHeight;
}

function appendPlayerCommand(cmd) {
  const div = document.createElement("div");
  div.className = "line player";
  div.textContent = `> ${cmd}`;
  outputEl.appendChild(div);
  outputEl.scrollTop = outputEl.scrollHeight;
}

async function loadPythonFiles(pyodide) {
  for (const path of PY_FILES) {
    const url = `${PY_ROOT}/${path}`;
    const resp = await fetch(url);
    if (!resp.ok) {
      console.error("Failed to fetch", url, resp.status);
      continue;
    }
    const code = await resp.text();

    // Ensure directory exists in Pyodide FS
    const segments = path.split("/");
    if (segments.length > 1) {
      const dir = segments.slice(0, -1).join("/");
      try {
        pyodide.FS.mkdir(dir);
      } catch (e) {
        // ignore if already exists
      }
    }

    pyodide.FS.writeFile(path, code);
  }
}

async function initPyodideAndGame() {
  statusEl.textContent = "Loading Pyodide…";
  const pyodide = await loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/",
  });

  statusEl.textContent = "Loading game files…";
  await loadPythonFiles(pyodide);

  statusEl.textContent = "Initializing game…";
  await pyodide.runPythonAsync(`
import web_main
from web_main import start, handle_input
`);

  statusEl.textContent = "Ready. Type a command to begin.";
  return pyodide;
}

async function ensurePyodide() {
  if (!pyodideReadyPromise) {
    pyodideReadyPromise = initPyodideAndGame().then(async (pyodide) => {
      // Call start() once to get the opening scene
      const events = await pyodide.runPythonAsync("start()");
      renderEvents(events);
      return pyodide;
    });
  }
  return pyodideReadyPromise;
}

function renderEvents(events) {
  if (!events) return;

  let jsEvents = events;
  if (typeof events.toJs === "function") {
    jsEvents = events.toJs({ deep: true });
    if (typeof events.destroy === "function") {
      events.destroy();
    }
  }

  for (const ev of jsEvents) {
    if (!ev) continue;

    const kind = ev.kind || "narration";
    const text = ev.text ?? "";   // allow empty string

    // Handle sentinel even if text is empty
    if (kind === "game_over") {
      gameOver = true;
      inputEl.disabled = true;
      if (submitBtn) submitBtn.disabled = true;
      statusEl.textContent = "Game over. Refresh the page to restart.";
      continue;
    }

    // For all *other* kinds, you can still skip empty text lines
    if (!text) continue;

    if (kind === "hint") {
      appendLine(text, "hint");
    } else if (kind === "debug") {
      continue;
    } else if (kind === "dialogue_npc") {
      appendLine(`[NPC] ${text}`, "dialogue_npc");
    } else {
      appendLine(text, kind);
    }
  }
}


formEl.addEventListener("submit", async (e) => {
  e.preventDefault();
  if (gameOver) return;
  const cmd = inputEl.value.trim();
  if (!cmd) return;

  appendPlayerCommand(cmd);
  inputEl.value = "";

  const pyodide = await ensurePyodide();
  pyodide.globals.set("command_text", cmd);
  const events = await pyodide.runPythonAsync("handle_input(command_text)");
  renderEvents(events);
});

window.addEventListener("load", async () => {
  appendLine("Initializing Vault 656 systems…", "system");
  await ensurePyodide();
  inputEl.focus();
});
