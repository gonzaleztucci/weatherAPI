from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Font: Arial, Bold, 16pt
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Bash Flags Cheat Sheet', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255) # Light blue background
        self.cell(0, 6, label, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, flag, name, works_with, desc):
        # Flag Column
        self.set_font('Courier', 'B', 11)
        self.cell(20, 10, flag, 0, 0)
        
        # Name Column
        self.set_font('Arial', 'B', 11)
        self.cell(40, 10, name, 0, 0)
        
        # Works With Column
        self.set_font('Arial', 'I', 10)
        self.cell(35, 10, f"({works_with})", 0, 0)
        
        # Description
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, desc)
        self.ln(2)

pdf = PDF()
pdf.add_page()

# --- CONTENT DATA ---
flags = [
    ("-h", "Human Readable", "ls, df, du", "Displays file sizes in KB, MB, GB instead of bytes."),
    ("-i", "Interactive", "rm, cp, mv", "Asks for confirmation before overwriting or deleting files."),
    ("-v", "Verbose", "mkdir, rm, cp", "Prints details of exactly what the command is doing."),
    ("-p", "Parents", "mkdir", "Creates parent directories automatically if they don't exist."),
    ("-r", "Recursive", "rm, cp, grep", "Applies the command to the folder and everything inside it."),
    ("-f", "Follow", "tail", "Keeps a file open to monitor new lines added (great for logs)."),
]

# --- RENDER TABLE ---
pdf.chapter_title("Essential Flags")

for item in flags:
    pdf.chapter_body(item[0], item[1], item[2], item[3])

# --- PRO TIP SECTION ---
pdf.ln(5)
pdf.chapter_title("Pro Tip: Combining Flags")
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 8, "You can combine flags into a single command.\nExample: ls -lah")
pdf.set_font('Courier', '', 10)
pdf.multi_cell(0, 8, "List (l) all files (a) with human-readable sizes (h).")

# Output the file
pdf.output('Bash_Flags_Cheat_Sheet.pdf')
print("Success! 'Bash_Flags_Cheat_Sheet.pdf' has been created in your folder.")