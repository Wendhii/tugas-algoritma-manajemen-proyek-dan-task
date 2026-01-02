projects = {}
tasks = {}

def menu():
    print("\n=== MENU UTAMA ===")
    print("1. CRUD Proyek")
    print("2. CRUD Task")
    print("3. Sorting")
    print("4. Searching")
    print("5. Laporan")
    print("0. Keluar")

# ================= PROYEK =================
def crud_proyek():
    print("\n--- CRUD PROYEK ---")
    print("1. Tambah")
    print("2. Tampilkan")
    print("3. Update")
    print("4. Hapus")
    choice = input("Pilih: ")

    if choice == "1":
        pid = input("ID Proyek: ")
        projects[pid] = {
            "nama proyek": input("Nama Proyek: "),
            "klien": input("Klien: "),
            "deadline": input("Deadline (DD-MM-YYYY): "),
            "status": input("Status: ")
        }
        print("Proyek ditambahkan")

    elif choice == "2":
        for pid, p in projects.items():
            print(pid, p)

    elif choice == "3":
        pid = input("ID Proyek: ")
        if pid in projects:
            projects[pid]["nama proyek"] = input("Nama proyek baru: ")
            projects[pid]["klien"] = input("Klien baru: ")
            projects[pid]["deadline"] = input("Deadline baru: ")
            projects[pid]["status"] = input("Status baru: ")
            print("Proyek diupdate")
        else:
            print("ID tidak ditemukan")

    elif choice == "4":
        pid = input("ID Proyek: ")
        projects.pop(pid, None)
        tasks.pop(pid, None)
        print("Proyek & task terkait dihapus")

# ================= TASK =================
def crud_task():
    pid = input("Masukkan ID Proyek: ")
    if pid not in projects:
        print("ID Proyek tidak valid")
        return

    tasks.setdefault(pid, [])

    print("\n--- CRUD TASK ---")
    print("1. Tambah")
    print("2. Tampilkan")
    print("3. Update")
    print("4. Hapus")
    choice = input("Pilih: ")

    if choice == "1":
        task = {
            "judul": input("Judul Task: "),
            "pic": input("PIC: "),
            "status": input("Status (Open/On Progress/Done): ")
        }
        tasks[pid].append(task)
        print("Task ditambahkan")

    elif choice == "2":
        for i, t in enumerate(tasks[pid]):
            print(i, t)

    elif choice == "3":
        for i, t in enumerate(tasks[pid]):
            print(i, t)
        idx = int(input("Index: "))
        tasks[pid][idx]["judul"] = input("Judul baru: ")
        tasks[pid][idx]["pic"] = input("PIC baru: ")
        tasks[pid][idx]["status"] = input("Status baru: ")
        print("Task diupdate")

    elif choice == "4":
        for i, t in enumerate(tasks[pid]):
            print(i, t)
        idx = int(input("Index: "))
        tasks[pid].pop(idx)
        print("Task dihapus")

# ================= SORTING =================
def sorting():
    print("\n--- SORTING ---")
    print("1. Proyek berdasarkan deadline")
    print("2. Task berdasarkan status")
    choice = input("Pilih: ")

    if choice == "1":
        for pid in sorted(projects, key=lambda x: projects[x]["deadline"]):
            print(pid, projects[pid])

    elif choice == "2":
        pid = input("ID Proyek: ")
        for t in sorted(tasks.get(pid, []), key=lambda x: x["status"]):
            print(t)

# ================= SEARCH =================
def searching():
    print("\n--- SEARCH ---")
    print("1. Cari Proyek (nama proyek/klien)")
    print("2. Cari Task berdasarkan PIC")
    choice = input("Pilih: ")

    if choice == "1":
        key = input("Keyword: ").lower()
        for pid, p in projects.items():
            if key in p["nama proyek"].lower() or key in p["klien"].lower():
                print(pid, p)

    elif choice == "2":
        pic = input("Nama PIC: ").lower()
        for pid, tlist in tasks.items():
            for t in tlist:
                if pic in t["pic"].lower():
                    print(pid, t)

# ================= LAPORAN =================
def laporan():
    print("\n--- LAPORAN ---")
    for pid, tlist in tasks.items():
        if not tlist:
            continue
        done = sum(1 for t in tlist if t["status"].lower() == "done")
        persen = (done / len(tlist)) * 100
        print(f"Proyek {pid}: {persen:.2f}% task selesai")

# ================= MAIN =================
while True:
    menu()
    pilih = input("Pilih menu: ")

    if pilih == "1":
        crud_proyek()
    elif pilih == "2":
        crud_task()
    elif pilih == "3":
        sorting()
    elif pilih == "4":
        searching()
    elif pilih == "5":
        laporan()
    elif pilih == "0":
        print("Keluar...")
        break
    else:
        print("Menu tidak valid")