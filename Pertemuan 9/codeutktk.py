import tkinter as tk

root = tk.Tk()

# ## Latihan 1 Membuat Widget Dasar
# WidgetDasarku = tk.Tk()
# WidgetDasarku.mainloop()

# ## Latihan 2 Membuat Canvas
# Kanvasku = tk.Canvas(root, height = 1080, width = 1928)
# Kanvasku.pack()

## Latihan 3 Membuat Canvas
Frameku = tk.Frame(root, bg='blue')
Frameku.place(relwidth = 0.8, relheight = 0.8)
# root.mainloop()

# ## Latihan 4a Membuat Button di Root
# Tombolku = tk.Button(root, text = 'Tes Tombol', bg = 'gray', fg = 'red')
# Tombolku.pack()

## Latihan 4b Membuat Button di Frame
Entryku = tk.Entry(Frameku, bg='green')
Entryku.pack()
root.mainloop()

