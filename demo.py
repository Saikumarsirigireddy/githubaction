from rich.console import Console
from rich.text import Text

console = Console()

text = Text("Hello, World!", style="bold magenta on cyan")
console.print(text)
