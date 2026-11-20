import tkinter as tk
from dataclasses import dataclass
from typing import Callable

SIDEBAR_BG = "#1e1b4b"
SIDEBAR_HOVER = "#2e2a73"
SIDEBAR_TEXT = "#c7d2fe"
PAGE_BG = "#f1f5f9"
CARD_BG = "#ffffff"
BORDER = "#e2e8f0"
TEXT = "#0f172a"
MUTED = "#64748b"
ACCENT = "#4f46e5"
ACCENT_HOVER = "#4338ca"
ERROR = "#dc2626"

FONT = "Segoe UI"
MONO = "Consolas"


def factorial(number: int) -> int:
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def primes_in_range(start: int, end: int) -> list[int]:
    return [number for number in range(start, end + 1) if is_prime(number)]


def fibonacci(terms: int) -> list[int]:
    series, current, following = [], 0, 1
    for _ in range(terms):
        series.append(current)
        current, following = following, current + following
    return series


def is_palindrome(text: str) -> bool:
    characters = [char.lower() for char in text if char.isalnum()]
    left, right = 0, len(characters) - 1
    while left < right:
        if characters[left] != characters[right]:
            return False
        left += 1
        right -= 1
    return True


def digit_sum(number: int) -> int:
    total = 0
    while number:
        number, digit = divmod(number, 10)
        total += digit
    return total


def pyramid(rows: int) -> str:
    return "\n".join(" " * (rows - row) + "*" * (2 * row - 1) for row in range(1, rows + 1))


def find_primes(start: int, end: int) -> str:
    if start > end:
        raise ValueError("'From' cannot be greater than 'To'.")
    primes = primes_in_range(start, end)
    return ", ".join(map(str, primes)) if primes else "No prime numbers in this range."


@dataclass(frozen=True)
class Field:
    label: str
    kind: str = "int"
    minimum: int = 0
    maximum: int = 100


def read_field(field: Field, raw: str) -> int | str:
    raw = raw.strip()
    if not raw:
        raise ValueError(f"{field.label} cannot be empty.")

    if field.kind == "text":
        if not any(char.isalnum() for char in raw):
            raise ValueError(f"{field.label} needs at least one letter or digit.")
        return raw

    try:
        value = int(raw)
    except ValueError:
        raise ValueError(f"{field.label} must be a whole number.") from None
    if not field.minimum <= value <= field.maximum:
        raise ValueError(f"{field.label} must be between {field.minimum} and {field.maximum}.")
    return value


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    fields: tuple[Field, ...]
    compute: Callable[..., str]
    example: tuple


TOOLS = (
    Tool(
        "Factorial Calculator",
        "Calculate the factorial of a whole number.",
        (Field("Number"),),
        lambda n: f"{n}! = {factorial(n)}",
        (5,),
    ),
    Tool(
        "Prime Finder",
        "Find every prime number within a range.",
        (Field("From", maximum=500), Field("To", maximum=500)),
        find_primes,
        (10, 50),
    ),
    Tool(
        "Fibonacci Generator",
        "Generate the Fibonacci sequence for a chosen number of terms.",
        (Field("Terms", minimum=1, maximum=50),),
        lambda n: ", ".join(map(str, fibonacci(n))),
        (10,),
    ),
    Tool(
        "Palindrome Checker",
        "Check whether a word or phrase reads the same backwards. Case, spaces and punctuation are ignored.",
        (Field("Text", kind="text"),),
        lambda text: "Palindrome" if is_palindrome(text) else "Not a palindrome",
        ("Never odd or even",),
    ),
    Tool(
        "Digit Sum",
        "Add up all the digits of a number.",
        (Field("Number", maximum=10**12),),
        lambda n: f"Digit sum of {n} = {digit_sum(n)}",
        (4821,),
    ),
    Tool(
        "Pyramid Generator",
        "Print a centred star pyramid with the number of rows you choose.",
        (Field("Rows", minimum=1, maximum=12),),
        pyramid,
        (4,),
    ),
)


class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, *, fill, hover, fg="white", width=120, height=42, radius=12):
        super().__init__(parent, width=width, height=height, bg=parent["bg"],
                         highlightthickness=0, cursor="hand2")
        corners = [(radius, 0), (width - radius, 0), (width, 0), (width, radius),
                   (width, height - radius), (width, height), (width - radius, height),
                   (radius, height), (0, height), (0, height - radius), (0, radius), (0, 0)]
        self.shape = self.create_polygon(corners, smooth=True, fill=fill, outline="")
        self.create_text(width / 2, height / 2, text=text, fill=fg, font=(FONT, 11, "bold"))

        self.bind("<Button-1>", lambda _event: command())
        self.bind("<Enter>", lambda _event: self.itemconfig(self.shape, fill=hover))
        self.bind("<Leave>", lambda _event: self.itemconfig(self.shape, fill=fill))


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("QuickTools")
        self.geometry("960x620")
        self.minsize(880, 580)
        self.configure(bg=PAGE_BG)

        self.index = 0
        self.nav_items: list[tk.Label] = []
        self.entries: list[tk.Entry] = []

        self._build_sidebar()
        self._build_content()
        self.bind("<Return>", lambda _event: self.calculate())
        self.show(0)

    @property
    def tool(self) -> Tool:
        return TOOLS[self.index]

    @staticmethod
    def _label(parent, text="", *, size=11, color=TEXT, bold=False, **options) -> tk.Label:
        return tk.Label(parent, text=text, bg=parent["bg"], fg=color, anchor="w", justify="left",
                        font=(FONT, size, "bold" if bold else "normal"), **options)

    def _build_sidebar(self) -> None:
        sidebar = tk.Frame(self, bg=SIDEBAR_BG, width=260)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        self._label(sidebar, "QuickTools", size=20, bold=True, color="white").pack(fill="x", padx=26, pady=(32, 0))
        self._label(sidebar, "Number & text utilities", size=10, color=SIDEBAR_TEXT).pack(fill="x", padx=26, pady=(2, 28))

        for index, tool in enumerate(TOOLS):
            item = tk.Label(sidebar, text=tool.name, anchor="w", bg=SIDEBAR_BG, fg=SIDEBAR_TEXT,
                            font=(FONT, 11), padx=18, pady=11, cursor="hand2")
            item.pack(fill="x", padx=14, pady=2)
            item.bind("<Button-1>", lambda _event, i=index: self.show(i))
            item.bind("<Enter>", lambda _event, i=index: self._hover(i, True))
            item.bind("<Leave>", lambda _event, i=index: self._hover(i, False))
            self.nav_items.append(item)

    def _build_content(self) -> None:
        content = tk.Frame(self, bg=PAGE_BG)
        content.pack(side="left", fill="both", expand=True, padx=40, pady=32)

        self.title_label = self._label(content, size=24, bold=True)
        self.title_label.pack(fill="x")
        self.description_label = self._label(content, color=MUTED, wraplength=620)
        self.description_label.pack(fill="x", pady=(4, 22))

        card = tk.Frame(content, bg=CARD_BG, highlightthickness=1, highlightbackground=BORDER, padx=22, pady=20)
        card.pack(fill="x")
        self.inputs_frame = tk.Frame(card, bg=CARD_BG)
        self.inputs_frame.pack(side="left")

        buttons = tk.Frame(card, bg=CARD_BG)
        buttons.pack(side="right", anchor="s")
        RoundedButton(buttons, "Use example", self.use_example, fill=BORDER, hover="#cbd5e1",
                      fg=TEXT, width=130, height=44).pack(side="left", padx=(0, 10))
        RoundedButton(buttons, "Calculate", self.calculate, fill=ACCENT, hover=ACCENT_HOVER,
                      width=120, height=44).pack(side="left")

        self.caption_label = self._label(content, size=10, bold=True)
        self.caption_label.pack(fill="x", pady=(26, 6))
        self.output = tk.Text(content, height=8, bg=CARD_BG, font=(MONO, 13), relief="flat",
                              padx=22, pady=18, wrap="word", state="disabled",
                              highlightthickness=1, highlightbackground=BORDER)
        self.output.pack(fill="both", expand=True)
        for tag, color in (("example", MUTED), ("result", TEXT), ("error", ERROR)):
            self.output.tag_configure(tag, foreground=color)

    def _hover(self, index: int, inside: bool) -> None:
        if index != self.index:
            self.nav_items[index].config(bg=SIDEBAR_HOVER if inside else SIDEBAR_BG)

    def show(self, index: int) -> None:
        self.index = index
        for position, item in enumerate(self.nav_items):
            active = position == index
            item.config(bg=ACCENT if active else SIDEBAR_BG, fg="white" if active else SIDEBAR_TEXT)

        tool = self.tool
        self.title_label.config(text=tool.name)
        self.description_label.config(text=tool.description)
        self._build_inputs()
        example_input = ", ".join(map(str, tool.example))
        self._show_output(f"Example result  -  input: {example_input}", tool.compute(*tool.example), "example")

    def _build_inputs(self) -> None:
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()
        self.entries.clear()

        for column, field in enumerate(self.tool.fields):
            group = tk.Frame(self.inputs_frame, bg=CARD_BG)
            group.grid(row=0, column=column, padx=(0, 16))
            self._label(group, field.label, size=10, color=MUTED).pack(fill="x", pady=(0, 4))
            entry = tk.Entry(group, width=22 if field.kind == "text" else 12, bg=PAGE_BG, fg=TEXT,
                             insertbackground=TEXT, relief="flat", font=(FONT, 13),
                             highlightthickness=1, highlightbackground=BORDER, highlightcolor=ACCENT)
            entry.pack(ipady=7)
            self.entries.append(entry)
        self.entries[0].focus_set()

    def use_example(self) -> None:
        for entry, value in zip(self.entries, self.tool.example):
            entry.delete(0, "end")
            entry.insert(0, str(value))
        self.calculate()

    def calculate(self) -> None:
        try:
            values = [read_field(field, entry.get())
                      for field, entry in zip(self.tool.fields, self.entries)]
            self._show_output("Result", self.tool.compute(*values), "result")
        except ValueError as error:
            self._show_output("Invalid input", str(error), "error")

    def _show_output(self, caption: str, text: str, tag: str) -> None:
        self.caption_label.config(text=caption, fg=ERROR if tag == "error" else MUTED)
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text, tag)
        self.output.config(state="disabled")


def enable_sharp_text() -> None:
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except (ImportError, AttributeError, OSError):
        pass


if __name__ == "__main__":
    enable_sharp_text()
    App().mainloop()