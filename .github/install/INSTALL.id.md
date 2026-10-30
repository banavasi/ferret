# Cara Menginstal

<details>
<summary><strong>Antigravity (<code>agy</code>)</strong></summary>

### Instalasi

```bash
agy plugin install https://github.com/banavasi/ferret
```

### Verifikasi

```bash
agy plugin list
```

### Pembaruan

```bash
agy plugin uninstall ferret
agy plugin install https://github.com/banavasi/ferret
```

### Uninstal

```bash
agy plugin uninstall ferret
```

Atau biarkan terinstal tetapi nonaktifkan: `agy plugin disable ferret`.

### Selalu Aktif (opsional)

Tambahkan ke `~/.gemini/GEMINI.md`:

```markdown
## Gaya Respons

Pembaca ini memiliki ADHD. Susun setiap respons agar mudah ditindaklanjuti, jangan bertele-tele yaaa:

1. Mulailah dengan jawaban atau langkah selanjutnya: perintah, jalur file, atau cuplikan kode terlebih dahulu.
2. Beri nomor pada pekerjaan yang memiliki beberapa langkah; batasi satu tindakan jelas per langkah.
3. Akhiri dengan satu tindakan selanjutnya yang bisa diselesaikan dalam waktu kurang dari dua menit.
4. Selesaikan masalah saat ini sebelum membahas masalah lain.
5. Tegaskan kembali progres di setiap giliran (misalnya, "langkah 3 dari 5 selesai").
6. Berikan estimasi waktu dalam satuan yang konkret, jangan pernah menggunakan kata seperti "sebentar".
7. Setelah ada perubahan, tunjukkan apa yang sekarang berhasil berfungsi.
8. Error: jelaskan lokasi, penyebab, dan solusinya, tanpa basa-basi.
9. Batasi daftar hanya hingga 5 item.
10. Tanpa pembukaan, ringkasan ulang, atau salam penutup.

Pengecualian: jelaskan secara lengkap jika diminta. Konfirmasi sebelum melakukan tindakan yang bersifat destruktif. Setelah tiga kali percobaan perbaikan yang gagal, berhentilah dan identifikasi asumsi yang meragukan. Jika permintaan ambigu, ajukan satu pertanyaan singkat.
```

</details>

<details>
<summary><strong>Claude Code</strong></summary>

### Instalasi

```bash
claude plugin marketplace add banavasi/ferret
claude plugin install ferret@ferret
```

Ketik `/ferret`.

### Verifikasi

```bash
claude plugin list
```

### Pembaruan

```bash
claude plugin marketplace update ferret
claude plugin update ferret@ferret
```

### Uninstal

```bash
claude plugin uninstall ferret
claude plugin marketplace remove ferret
```

Atau biarkan terinstal tetapi nonaktifkan: `claude plugin disable ferret`.

### Selalu Aktif (opsional)

Hook `SessionStart` akan memuat semua aturan di awal setiap sesi; Anda tidak perlu lagi mengetik `/ferret`:

```bash
touch ~/.claude/.ferret-always
```

Jika Anda menggunakan direktori konfigurasi kustom untuk Claude, buat file penanda (flag) di dalamnya:

```bash
touch "$CLAUDE_CONFIG_DIR/.ferret-always"
```

Untuk kembali ke mode sesuai permintaan (on-demand):

```bash
rm ~/.claude/.ferret-always
```

Hook ini hanya berjalan ketika file penanda ada, jadi menginstal plugin saja tidak akan mengubah apa pun. Perintah "normal mode" tetap akan menonaktifkannya di sesi saat ini.

</details>

<details>
<summary><strong>Codex</strong></summary>

### Instalasi

```bash
codex plugin marketplace add banavasi/ferret --ref main
codex plugin add ferret@ferret
```

Aktifkan skill ini secara eksplisit dengan mengetik `$ferret`. Codex ga bakalan memanggilnya secara otomatis.

### Verifikasi

```bash
codex plugin list
```

### Pembaruan

```bash
codex plugin marketplace upgrade ferret
codex plugin remove ferret
codex plugin add ferret@ferret
```

### Uninstal

```bash
codex plugin remove ferret
codex plugin marketplace remove ferret
```

### Selalu Aktif (opsional)

Tambahkan ke `~/.codex/AGENTS.md`:

```markdown
## Gaya Respons

Pembaca memiliki ADHD. Susun setiap respons agar mudah ditindaklanjuti:

1. Mulailah dengan jawaban atau langkah selanjutnya: perintah, jalur file, atau cuplikan kode terlebih dahulu.
2. Beri nomor pada pekerjaan yang memiliki beberapa langkah; batasi satu tindakan jelas per langkah.
3. Akhiri dengan satu tindakan selanjutnya yang bisa diselesaikan dalam waktu kurang dari dua menit.
4. Selesaikan masalah saat ini sebelum membahas masalah lain.
5. Tegaskan kembali progres di setiap giliran (misalnya, "langkah 3 dari 5 selesai").
6. Berikan estimasi waktu dalam satuan yang konkret, jangan pernah menggunakan kata seperti "sebentar".
7. Setelah ada perubahan, tunjukkan apa yang sekarang berhasil berfungsi.
8. Error: jelaskan lokasi, penyebab, dan solusinya, tanpa basa-basi.
9. Batasi daftar hanya hingga 5 item.
10. Tanpa pembukaan, ringkasan ulang, atau salam penutup.

Pengecualian: jelaskan secara lengkap jika diminta. Konfirmasi sebelum melakukan tindakan yang bersifat destruktif. Setelah tiga kali percobaan perbaikan yang gagal, berhentilah dan identifikasi asumsi yang meragukan. Jika permintaan ambigu, ajukan satu pertanyaan singkat.
```

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

Gemini CLI tidak memiliki marketplace plugin, jadi ada dua opsi bawaan: perintah kustom (opt-in, nonaktif sampai dipanggil) atau ekstensi (selalu aktif setelah diinstal). Perintah ini sesuai dengan perilaku bawaan skill ini; pilih ini kecuali Anda ingin aturannya berlaku di semua sesi.

### Instalasi (perintah, opt-in)

```bash
mkdir -p ~/.gemini/commands
curl -fsSL https://raw.githubusercontent.com/banavasi/ferret/main/skills/ferret/agents/gemini.toml \
  -o ~/.gemini/commands/ferret.toml
```

Mulai sesi baru dan ketik `/ferret`. Skill ini akan tetap aktif selama sesi tersebut.

### Instalasi (ekstensi, always-on)

```bash
gemini extensions install https://github.com/banavasi/ferret
```

Ekstensi ini memuat `GEMINI.md`, yang mengimpor skill secara lengkap; dengan demikian, aturannya berlaku sejak pesan pertama. Git harus sudah terinstal.

### Verifikasi

```bash
gemini extensions list          # via ekstensi
ls ~/.gemini/commands           # rute perintah: ferret.toml ada
```

Atau ketik `/` di dalam sesi dan pastikan `ferret` muncul dalam daftar.

### Pembaruan

```bash
gemini extensions update ferret    # via ekstensi
# via perintah: jalankan ulang perintah curl di atas
```

### Uninstal

```bash
gemini extensions uninstall ferret    # via ekstensi
rm ~/.gemini/commands/ferret.toml     # rute perintah
```

</details>

<details>
<summary><strong>GitHub Copilot (VS Code dan Copilot CLI)</strong></summary>

Copilot membaca Agent Skills secara native: menggunakan file `SKILL.md` yang sama, tanpa konversi. Di dalam proyek, ia memeriksa `.github/skills/`, `.claude/skills/`, dan `.agents/skills/`; secara global, ia memeriksa `~/.copilot/skills/`, `~/.claude/skills/`, dan `~/.agents/skills/`.

### Instalasi

```bash
npx skills add banavasi/ferret -a github-copilot        # proyek ini
npx skills add banavasi/ferret -a github-copilot -g     # semua proyek
```

Tanpa CLI, salin folder skill ke direktori mana pun yang diperiksa oleh Copilot:

```bash
git clone https://github.com/banavasi/ferret
mkdir -p ~/.copilot/skills
cp -R ferret/skills/ferret ~/.copilot/skills/
```

### Verifikasi

Ketik `/` di kolom obrolan dan pastikan `ferret` muncul. Atau:

```bash
npx skills list
npx skills ls -g    # jika diinstal secara global
```

### Pembaruan

```bash
npx skills update ferret
```

Atau salin ulang foldernya setelah `git pull`.

### Uninstal

```bash
npx skills remove ferret
```

Atau hapus folder `ferret` dari direktori skill tempat ia diinstal.

### Catatan tentang aktivasi

Copilot menghormati `disable-model-invocation`: tidak ada yang diterapkan sampai Anda memanggil skill tersebut, sama seperti di Claude Code (telah diuji pada [#60](https://github.com/banavasi/ferret/pull/60)).

### Selalu Aktif (opsional)

Tambahkan blok di bawah ini ke `.github/copilot-instructions.md` pada proyek Anda (Copilot akan membacanya di setiap obrolan):

```markdown
## Gaya Respons

Pembaca memiliki ADHD. Susun setiap respons agar mudah ditindaklanjuti:

1. Mulailah dengan jawaban atau langkah selanjutnya: perintah, jalur file, atau cuplikan kode terlebih dahulu.
2. Beri nomor pada pekerjaan yang memiliki beberapa langkah; batasi satu tindakan jelas per langkah.
3. Akhiri dengan satu tindakan selanjutnya yang bisa diselesaikan dalam waktu kurang dari dua menit.
4. Selesaikan masalah saat ini sebelum membahas masalah lain.
5. Tegaskan kembali progres di setiap giliran (misalnya, "langkah 3 dari 5 selesai").
6. Berikan estimasi waktu dalam satuan yang konkret, jangan pernah menggunakan kata seperti "sebentar".
7. Setelah ada perubahan, tunjukkan apa yang sekarang berhasil berfungsi.
8. Error: jelaskan lokasi, penyebab, dan solusinya, tanpa basa-basi.
9. Batasi daftar hanya hingga 5 item.
10. Tanpa pembukaan, ringkasan ulang, atau salam penutup.

Pengecualian: jelaskan secara lengkap jika diminta. Konfirmasi sebelum melakukan tindakan yang bersifat destruktif. Setelah tiga kali percobaan perbaikan yang gagal, berhentilah dan identifikasi asumsi yang meragukan. Jika permintaan ambigu, ajukan satu pertanyaan singkat.
```

</details>

<details>
<summary><strong>Hermes</strong></summary>

### Instalasi

```bash
hermes skills install banavasi/ferret/skills/ferret
```

Ketik `/ferret`. Skill ini akan diinstal ke `~/.hermes/skills/` dan tersedia sebagai perintah slash saat sesi berikutnya dimulai.

Lebih suka menjelajah dulu? Tambahkan repositori ini sebagai sumber skill (sebagai "tap"), lalu cari dan instal:

```bash
hermes skills tap add banavasi/ferret
hermes skills search ferret
hermes skills install banavasi/ferret/skills/ferret
```

### Verifikasi

```bash
hermes skills list
```

### Pembaruan

```bash
hermes skills update ferret
```

### Uninstal

```bash
hermes skills uninstall ferret
```

Atau hapus juga tap-nya: `hermes skills tap remove banavasi/ferret`.

### Selalu Aktif (opsional)

Tambahkan ke `AGENTS.md` di direktori kerja Anda (Hermes memuatnya per direktori) atau ke `SOUL.md` pada persona Anda untuk semua sesi:

```markdown
## Gaya Respons

Pembaca memiliki ADHD. Susun setiap respons agar mudah ditindaklanjuti:

1. Mulailah dengan jawaban atau langkah selanjutnya: perintah, jalur file, atau cuplikan kode terlebih dahulu.
2. Beri nomor pada pekerjaan yang memiliki beberapa langkah; batasi satu tindakan jelas per langkah.
3. Akhiri dengan satu tindakan selanjutnya yang bisa diselesaikan dalam waktu kurang dari dua menit.
4. Selesaikan masalah saat ini sebelum membahas masalah lain.
5. Tegaskan kembali progres di setiap giliran (misalnya, "langkah 3 dari 5 selesai").
6. Berikan estimasi waktu dalam satuan yang konkret, jangan pernah menggunakan kata seperti "sebentar".
7. Setelah ada perubahan, tunjukkan apa yang sekarang berhasil berfungsi.
8. Error: jelaskan lokasi, penyebab, dan solusinya, tanpa basa-basi.
9. Batasi daftar hanya hingga 5 item.
10. Tanpa pembukaan, ringkasan ulang, atau salam penutup.

Pengecualian: jelaskan secara lengkap jika diminta. Konfirmasi sebelum melakukan tindakan yang bersifat destruktif. Setelah tiga kali percobaan perbaikan yang gagal, berhentilah dan identifikasi asumsi yang meragukan. Jika permintaan ambigu, ajukan satu pertanyaan singkat.
```

</details>

<details>
<summary><strong>Kimi Code CLI</strong></summary>

### Instalasi

Mulai sesi Kimi Code dan:

1. Jalankan `/plugins`.
2. Pilih **Custom**.
3. Tempel `https://github.com/banavasi/ferret` dan tekan Enter.
4. Pilih **Trust and install**.

Gunakan perintah slash `/skill:ferret` untuk memanggil skill ini secara eksplisit.

### Pembaruan

Di dalam sesi Kimi Code, jalankan `/plugins`, arahkan kursor ke **Ferret**, dan tekan `R`.

### Uninstal

Di dalam sesi Kimi Code, jalankan `/plugins`, arahkan kursor ke **Ferret**, dan tekan `D`.

</details>

<details>
<summary><strong>OpenCode</strong></summary>

Plugin mendukung OpenCode V1 **1.18.29 atau lebih baru** dan V2. Plugin mendaftarkan skill dan perintah `/ferret`, serta menyediakan mode selalu aktif opsional. Versi V1 yang lebih lama perlu diperbarui atau menggunakan plugin dari rilis skill sebelumnya.

### Instalasi

Untuk digunakan di semua proyek:

```bash
git clone https://github.com/banavasi/ferret ~/.config/opencode/vendor/ferret
mkdir -p ~/.config/opencode/plugins
cat > ~/.config/opencode/plugins/ferret.js <<'EOF'
export { default } from '../vendor/ferret/.opencode/plugins/ferret.mjs';
EOF
```

Untuk instalasi V1 yang sudah ada, pertahankan entri `plugin` di `opencode.json`. Jika beralih ke pemuat di atas, hapus entri tersebut.

Mulai sesi baru dan ketik `/ferret`. Aturan berlaku hingga Anda mengatakan `normal mode` atau `normal mode`.

#### Hanya skill dan perintah (tanpa mode selalu aktif)

Sebagai alternatif, salin skill dan perintah dari repositori ke direktori global OpenCode:

```bash
mkdir -p ~/.config/opencode/skills/ferret ~/.config/opencode/commands
cp skills/ferret/SKILL.md ~/.config/opencode/skills/ferret/SKILL.md
cp .opencode/command/ferret.md ~/.config/opencode/commands/ferret.md
```

### Verifikasi

Jalankan OpenCode, ketik `/`, dan pastikan `ferret` muncul dalam daftar perintah.

### Pembaruan

```bash
git -C ~/.config/opencode/vendor/ferret pull
```

Untuk instalasi dengan menyalin, perbarui repositori lalu salin kembali kedua file.

### Uninstal

Hapus `~/.config/opencode/plugins/ferret.js`. Untuk instalasi dengan menyalin, hapus `~/.config/opencode/skills/ferret/` dan `~/.config/opencode/commands/ferret.md`. Untuk instalasi V1 dengan konfigurasi yang sudah ada, hapus entri `plugin` terkait.

### Selalu Aktif (opsional)

Memerlukan plugin. Membuat file penanda menambahkan seluruh aturan ke prompt sistem pada setiap giliran:

```bash
touch ~/.config/opencode/.ferret-always
```

`normal mode` atau `normal mode` meminta agen kembali ke gaya respons biasa untuk sesi saat ini. Hapus file penanda untuk menghentikan penyisipan otomatis:

```bash
rm ~/.config/opencode/.ferret-always
```

Jika `XDG_CONFIG_HOME` diatur, ganti `~/.config` dalam jalur ini dengan direktori tersebut.

</details>

<details>
<summary><strong>Pi</strong></summary>

Pi mengimplementasikan standar Agent Skills, sehingga file `SKILL.md` yang sama dimuat langsung tanpa konversi. Cara pemanggilan di Pi sedikit berbeda: skill dipanggil dengan format `/skill:<nama>`.

### Instalasi

```bash
npx skills add banavasi/ferret -a pi -y
```

Lebih suka menggunakan sistem file? Pi menemukan skill di `~/.pi/agent/skills/` dan `~/.agents/skills/` (global), serta di `.pi/skills/` dan `.agents/skills/` (proyek):

```bash
git clone https://github.com/banavasi/ferret
mkdir -p ~/.pi/agent/skills
cp -R ferret/skills/ferret ~/.pi/agent/skills/
```

Aktifkan perintah slash untuk skill di `settings.json` Pi:

```json
{ "enableSkillCommands": true }
```

Mulai sesi baru dan ketik `/skill:ferret`.

### Verifikasi

```bash
npx skills list
```

Atau ketik `/skill:` di dalam sesi dan pastikan `ferret` muncul dalam daftar.

### Pembaruan

```bash
npx skills update ferret
```

Atau salin ulang foldernya setelah `git pull`.

### Uninstal

```bash
npx skills remove ferret
```

Atau hapus `~/.pi/agent/skills/ferret`.

### Selalu Aktif (opsional)

Tambahkan ke `AGENTS.md` pada proyek Anda:

```markdown
## Gaya Respons

Pembaca memiliki ADHD. Susun setiap respons agar mudah ditindaklanjuti:

1. Mulailah dengan jawaban atau langkah selanjutnya: perintah, jalur file, atau cuplikan kode terlebih dahulu.
2. Beri nomor pada pekerjaan yang memiliki beberapa langkah; batasi satu tindakan jelas per langkah.
3. Akhiri dengan satu tindakan selanjutnya yang bisa diselesaikan dalam waktu kurang dari dua menit.
4. Selesaikan masalah saat ini sebelum membahas masalah lain.
5. Tegaskan kembali progres di setiap giliran (misalnya, "langkah 3 dari 5 selesai").
6. Berikan estimasi waktu dalam satuan yang konkret, jangan pernah menggunakan kata seperti "sebentar".
7. Setelah ada perubahan, tunjukkan apa yang sekarang berhasil berfungsi.
8. Error: jelaskan lokasi, penyebab, dan solusinya, tanpa basa-basi.
9. Batasi daftar hanya hingga 5 item.
10. Tanpa pembukaan, ringkasan ulang, atau salam penutup.

Pengecualian: jelaskan secara lengkap jika diminta. Konfirmasi sebelum melakukan tindakan yang bersifat destruktif. Setelah tiga kali percobaan perbaikan yang gagal, berhentilah dan identifikasi asumsi yang meragukan. Jika permintaan ambigu, ajukan satu pertanyaan singkat.
```

</details>

<details>
<summary><strong>Qwen Code</strong></summary>

### Instalasi

```bash
qwen extensions install banavasi/ferret
```

Qwen Code menerima format singkat GitHub dan menginstal repositori sebagai ekstensi native. Ekstensi ini akan menemukan skill di dalam `skills/`.

Ketik `/ferret` untuk memanggil skill ini secara eksplisit. Menginstal ekstensi gak bakal mengubah keluaran sampai skill tersebut dipanggil.

### Verifikasi

```bash
qwen extensions list
```

Selanjutnya, mulai sesi baru Qwen Code dan jalankan:

```text
/skills
```

Pastikan `ferret` muncul dalam daftar.

### Pembaruan

```bash
qwen extensions update ferret
```

### Uninstal

```bash
qwen extensions uninstall ferret
```

</details>

<details>
<summary><strong>Zed</strong></summary>

Zed Agent membaca Agent Skills secara native: menggunakan file `SKILL.md` yang sama, tanpa konversi. ("Rules" lama di Zed telah digantikan oleh Skills dan instruksi di `AGENTS.md`.)

### Instalasi

Di Agent Panel, buka pengelola Skills, pilih **Create skill from URL** (juga tersedia di palet sebagai `agent: create skill from url`) dan tempel:

```
https://github.com/banavasi/ferret/blob/main/skills/ferret/SKILL.md
```

Simpan dengan cakupan **User** untuk semua proyek, atau **Project** untuk satu proyek tertentu. Setelah itu, ketik `/ferret` di Agent Panel.

Lebih suka menggunakan sistem file? Klon repositori dan letakkan folder skill di direktori skill pengguna:

```bash
git clone https://github.com/banavasi/ferret
mkdir -p ~/.agents/skills
cp -R ferret/skills/ferret ~/.agents/skills/
```

### Verifikasi

Buka pengelola Skills di Agent Panel dan pastikan `ferret` muncul. Atau ketik `/` dan periksa.

### Pembaruan

Impor ulang menggunakan URL yang sama (akan menimpa) atau salin ulang foldernya setelah `git pull`.

### Uninstal

Hapus `ferret` dari pengelola Skills atau hapus folder `~/.agents/skills/ferret`.

### Selalu Aktif (opsional)

Tambahkan ke file `~/.config/zed/AGENTS.md` pribadi Anda:

```markdown
## Gaya Respons

Pembaca memiliki ADHD. Susun setiap respons agar mudah ditindaklanjuti:

1. Mulailah dengan jawaban atau langkah selanjutnya: perintah, jalur file, atau cuplikan kode terlebih dahulu.
2. Beri nomor pada pekerjaan yang memiliki beberapa langkah; batasi satu tindakan jelas per langkah.
3. Akhiri dengan satu tindakan selanjutnya yang bisa diselesaikan dalam waktu kurang dari dua menit.
4. Selesaikan masalah saat ini sebelum membahas masalah lain.
5. Tegaskan kembali progres di setiap giliran (misalnya, "langkah 3 dari 5 selesai").
6. Berikan estimasi waktu dalam satuan yang konkret, jangan pernah menggunakan kata seperti "sebentar".
7. Setelah ada perubahan, tunjukkan apa yang sekarang berhasil berfungsi.
8. Error: jelaskan lokasi, penyebab, dan solusinya, tanpa basa-basi.
9. Batasi daftar hanya hingga 5 item.
10. Tanpa pembukaan, ringkasan ulang, atau salam penutup.

Pengecualian: jelaskan secara lengkap jika diminta. Konfirmasi sebelum melakukan tindakan yang bersifat destruktif. Setelah tiga kali percobaan perbaikan yang gagal, berhentilah dan identifikasi asumsi yang meragukan. Jika permintaan ambigu, ajukan satu pertanyaan singkat.
```

</details>

<details>
<summary><strong>Cursor, Amp, dan lingkungan lain yang kompatibel dengan agent-skills</strong></summary>

Berfungsi di lingkungan apa pun yang mendukung pembacaan Agent Skills. Ganti `-a <agent>` dengan agen pilihan Anda.

### Instalasi

```bash
npx skills add banavasi/ferret                  # workspace ini
npx skills add banavasi/ferret -g               # semua proyek
npx skills add banavasi/ferret -a cursor -y     # satu agen saja
npx skills add banavasi/ferret -a opencode -y
```

Buka obrolan agen baru dan ketik `/ferret`.

Tanpa CLI, salin folder skill ke jalur yang diperiksa oleh agen Anda:

```bash
git clone https://github.com/banavasi/ferret
mkdir -p ~/.cursor/skills     # Cursor. Gunakan .agents/skills di OpenCode atau jalur khusus agen Anda
cp -R ferret/skills/ferret ~/.cursor/skills/
```

### Verifikasi

```bash
npx skills list
npx skills ls -g    # jika diinstal secara global
```

### Pembaruan

```bash
npx skills update ferret
npx skills update -g    # jika diinstal secara global
```

### Uninstal

```bash
npx skills remove ferret
npx skills remove ferret -g    # jika diinstal secara global
```

### Selalu Aktif (opsional)

Tempel ini ke file aturan agen yang persisten. Cursor: **Settings → Rules → User Rules**, atau aturan proyek di `.cursor/rules/` dengan `alwaysApply: true`. OpenCode: `~/.config/opencode/AGENTS.md`.

```markdown
## Gaya Respons

Pembaca memiliki ADHD. Susun setiap respons agar mudah ditindaklanjuti:

1. Mulailah dengan jawaban atau langkah selanjutnya: perintah, jalur file, atau cuplikan kode terlebih dahulu.
2. Beri nomor pada pekerjaan yang memiliki beberapa langkah; batasi satu tindakan jelas per langkah.
3. Akhiri dengan satu tindakan selanjutnya yang bisa diselesaikan dalam waktu kurang dari dua menit.
4. Selesaikan masalah saat ini sebelum membahas masalah lain.
5. Tegaskan kembali progres di setiap giliran (misalnya, "langkah 3 dari 5 selesai").
6. Berikan estimasi waktu dalam satuan yang konkret, jangan pernah menggunakan kata seperti "sebentar".
7. Setelah ada perubahan, tunjukkan apa yang sekarang berhasil berfungsi.
8. Error: jelaskan lokasi, penyebab, dan solusinya, tanpa basa-basi.
9. Batasi daftar hanya hingga 5 item.
10. Tanpa pembukaan, ringkasan ulang, atau salam penutup.

Pengecualian: jelaskan secara lengkap jika diminta. Konfirmasi sebelum melakukan tindakan yang bersifat destruktif. Setelah tiga kali percobaan perbaikan yang gagal, berhentilah dan identifikasi asumsi yang meragukan. Jika permintaan ambigu, ajukan satu pertanyaan singkat.
```
</details>


## Cara Kerja Aktivasi

1. **Terinstal, tetapi tidak dipanggil.** Di Claude Code, Qwen Code, dan Codex, tidak ada yang terjadi sampai Anda memanggil skill ini secara eksplisit. Claude Code dan Qwen Code menghormati `disable-model-invocation: true` di `SKILL.md`; Codex menghormati `policy.allow_implicit_invocation: false` di `agents/openai.yaml`. Lingkungan lain mungkin memuat deskripsi setiap skill saat startup dan mengaktifkannya sendiri.
2. **Anda memanggilnya secara eksplisit.** Ketik `/ferret` di Claude Code atau Qwen Code, atau `$ferret` di Codex. Aturan ini bakalan aktif di sesi tersebut. Perintah "normal mode" atau "normal mode" bakal menonaktifkannya.
3. **Anda membuat `~/.claude/.ferret-always`** (Claude Code). Hook `SessionStart` bakalan memuat (load) semua aturan sejak pesan pertama, di setiap sesi.
4. **Anda menambahkan cuplikan "selalu aktif" di atas** (lingkungan lain). Ini akan menjaga aturan utama tetap berada dalam konteks agen yang persisten.

Di Claude Code, Qwen Code, dan Codex gak ada jalan tengah: jikalau Anda tidak mengaktifkannya, maka skill ini nonaktif.

## Pemecahan Masalah (Troubleshooting)

**`/ferret` tidak muncul di pelengkapan otomatis (autocomplete).** Mulai ulang agen Anda. Indeks plugin dibaca saat startup.

**Flag selalu aktif tidak berfungsi.** Perbarui plugin (`claude plugin marketplace update ferret`, lalu `claude plugin update ferret@ferret`) dan mulai ulang. Hook dibaca saat startup, dan flag ini memerlukan versi yang menyertakan `hooks/hooks.json`.

**`claude plugin marketplace add` gagal.** Gunakan format `owner/repo`. Jalur lokal harus mengarah ke root repositori, bukan ke `.claude-plugin/`.

**Sudah diinstal, tetapi respons masih memiliki pembukaan (preambulo).** Buka sesi baru. Jika masih terus menyimpang, pertegas teks di `skills/ferret/SKILL.md`.

**Ingin peraturan yang berbeda?.** Lakukan fork skill ini, edit `skills/ferret/SKILL.md` sesuai keinginan, lalu ganti dengan salinan Anda sendiri:

```bash
claude plugin uninstall ferret            # hapus dulu salinan upstream:
claude plugin marketplace remove ferret   # fork dan upstream menggunakan nama yang sama
claude plugin marketplace add <username-anda>/ferret
claude plugin install ferret@ferret
```

Mulai ulang dan panggillah `/ferret` lagi.

**Skill tidak muncul setelah `npx skills add`.** Buka obrolan agen baru. Skill diindeks di awal sesi. Pastikan folder telah diinstal di lokasi yang dicari oleh agen (`~/.cursor/skills/` di Cursor, `.agents/skills/` di OpenCode) dan bahwa `name` di frontmatter sesuai dengan nama folder.
