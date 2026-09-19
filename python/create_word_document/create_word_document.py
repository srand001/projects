

# This Python script creates a Microsoft Word document.
# Complete with font sizes and bullet points.
# Designed by Surjit Randhawa 2026

# pip install python-docx


import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_harry_potter_doc():
    # Initialise document
    doc = docx.Document()
    
    # ----------------------------------------------------
    # Styles Setup
    # ----------------------------------------------------
    # Title Style
    style_title = doc.styles.add_style('Book Title Main', docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
    style_title.font.name = 'Arial'
    style_title.font.size = Pt(18)
    style_title.font.bold = True
    style_title.font.color.rgb = RGBColor(0, 0, 0)
    
    # Subtitle Style
    style_sub = doc.styles.add_style('Book Subtitle', docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
    style_sub.font.name = 'Arial'
    style_sub.font.size = Pt(14)
    style_sub.font.italic = True
    style_sub.font.color.rgb = RGBColor(100, 100, 100)
    
    # Heading Style
    style_h1 = doc.styles.add_style('Section Heading', docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
    style_h1.font.name = 'Arial'
    style_h1.font.size = Pt(16)
    style_h1.font.bold = True
    style_h1.font.color.rgb = RGBColor(0, 0, 0)
    
    # Body/List Style
    style_body = doc.styles['Normal']
    style_body.font.name = 'Arial'
    style_body.font.size = Pt(11)

    # ----------------------------------------------------
    # Content Generation
    # ----------------------------------------------------
    # Main Header
    title = doc.add_paragraph("Harry Potter and the Philosopher's Stone", style='Book Title Main')
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    
    subtitle = doc.add_paragraph("J.K. Rowling - 1997", style='Book Subtitle')
    doc.add_paragraph() # Spacer

    # Section 1: Key Characters
    doc.add_paragraph("Key Characters", style='Section Heading')
    
    characters = [
        ("Harry Potter", "The protagonist of the book, known in the wizarding world as 'The Boy Who Lived'."),
        ("Ron Weasley", "Harry's ultimate best friend. He comes from a large, loving, but impoverished pure-blood wizarding family."),
        ("Hermione Granger", "A brilliant, Muggle-born witch who initial appears bossy and overly concerned with rules."),
        ("Albus Dumbledore", "The venerable, eccentric, and widely respected Headmaster of Hogwarts."),
        ("Rubeus Hagrid", "The giant, warm-hearted Keeper of Keys and Grounds at Hogwarts."),
        ("Professor Severus Snape", "The sinister and strict Potions Master and Head of Slytherin House."),
        ("Professor Minerva McGonagall", "The stern but fair Deputy Headmistress and Head of Gryffindor House.")
    ]
    
    for name, desc in characters:
        p = doc.add_paragraph(style='List Bullet')
        p.add_run(f"{name}: ").bold = True
        p.add_run(desc)
        
    doc.add_paragraph() # Spacer

    # Section 2: Summary
    doc.add_paragraph("Summary", style='Section Heading')
    
    summary_points = [
        "Harry Potter is an orphaned boy living a miserable life with his cruel aunt, uncle, and cousin, the Dursleys.",
        "He spends ten years sleeping in a cramped cupboard under the stairs, completely unaware of his true identity.",
        "Mysterious letters written in green ink begin arriving for Harry, which his uncle desperately tries to destroy.",
        "On Harry's eleventh birthday, a gentle giant named Hagrid tracks him down to deliver the letter in person.",
        "Hagrid reveals the life-changing truth: Harry is a wizard, and he has been accepted into Hogwarts School of Witchcraft and Wizardry.",
        "Harry also learns his parents didn't die in a car crash; they were murdered by the dark wizard Lord Voldemort.",
        "Voldemort tried to kill baby Harry too, but the curse rebounded, leaving Harry with a lightning-bolt scar and immense fame.",
        "Hagrid takes Harry to Diagon Alley to buy his school supplies, including a wand and a snowy owl named Hedwig.",
        "On the Hogwarts Express, Harry makes fast friends with Ron Weasley and the brilliant Hermione Granger.",
        "Upon arriving at the castle, the Sorting Hat places all three friends into Gryffindor House.",
        "Harry settles into school life, learning magic, dealing with the strict Professor Snape, and joining the Quidditch team.",
        "The trio discovers a giant three-headed dog guarding a hidden trapdoor on the forbidden third-floor corridor.",
        "They learn the dog is protecting the Philosopher's Stone, a legendary artifact that grants eternal life.",
        "Harry, Ron, and Hermione mistakenly suspect that Professor Snape is trying to steal the Stone for Voldemort.",
        "When Headmaster Albus Dumbledore leaves the school, the kids realize the theft will happen that very night.",
        "They sneak past the dog and navigate a gauntlet of magical traps, including a deadly, life-sized game of wizard's chess.",
        "Ron and Hermione sacrifice themselves to let Harry pass, leaving him to enter the final chamber alone.",
        "Harry is shocked to find the stuttering Professor Quirrell, who is being possessed by Lord Voldemort's face on the back of his head.",
        "Quirrell tries to kill Harry, but Harry's skin blisters Quirrell's hands due to a lingering magical protection left by his mother's love.",
        "Voldemort's spirit flees, the Stone is destroyed, and Gryffindor wins the House Cup at the end-of-year feast."
    ]
    
    for point in summary_points:
        doc.add_paragraph(point, style='List Bullet')

    # Save document
    doc.save("Harry_Potter_Summary.docx")
    print("Document successfully created as 'Harry_Potter_Summary.docx'")

if __name__ == "__main__":
    create_harry_potter_doc()

