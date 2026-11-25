# SUBMIT README — Pigeon Pitch, One Line

- Slug: u-donrulezz-pigeon-pitch-one-line-af06c6cf
- Judul: Pigeon Pitch, One Line
- Repo: yudhisutawan77/makefun-pigeon-pitch
- Pot: $2 (top 10)
- Deadline: 27 Nov 2026 04:25 WITA

## Entry text (satu baris, 161 karakter)

I'm Pidge, founder of Crumb Capital: two million city pigeons deliver anything across rooftops for crumbs — zero CAC, infinite scale, and we're raising one loaf.

Jumlah karakter: 161 (maksimal 200). Satu baris.

## Daftar file

- main.py — entrypoint; menulis entry text ke $ENTRY_OUT (path file atau
  direktori → entry.txt; tanpa env → entry.txt di cwd) dan print ke stdout.
  Memvalidasi pitch satu baris ≤200 karakter sebelum menulis.
- README.md — 3 badge make.fun (dengan segmen slug kompetisi) + link make.fun.
- LICENSE — lisensi MIT, Copyright (c) 2026 yudhisutawan77.
- .makefun/owner.json — 57 byte, tanpa trailing newline.
- SUBMIT-README.md — file ini.

## Verifikasi yang sudah dijalankan

- `ENTRY_OUT=<file>` → file berisi persis satu baris entry text.
- `ENTRY_OUT=<direktori>` → `<direktori>/entry.txt` berisi persis satu baris entry text.
- Tanpa `ENTRY_OUT` → `entry.txt` di cwd berisi persis satu baris entry text.
- `wc -c .makefun/owner.json` → 57 byte; `od -c` mengonfirmasi akhir file `}` tanpa newline.
