# كيفية التثبيت

<details>
<summary><strong>Antigravity (<code>agy</code>)</strong></summary>

### تثبيت

```bash
agy plugin install https://github.com/banavasi/ferret
```

### تحقق

```bash
agy plugin list
```

### تحديث

```bash
agy plugin uninstall ferret
agy plugin install https://github.com/banavasi/ferret
```

### إلغاء التثبيت

```bash
agy plugin uninstall ferret
```

أو أبقِه مثبتًا وأوقف تشغيله: `agy plugin disable ferret`.

### تشغيل دائمًا (اختياري)

أضف إلى `~/.gemini/GEMINI.md`:

```markdown
## أسلوب الإجابة

القارئ مصاب باضطراب فرط الحركة وتشتت الانتباه. صُغ كل إجابة بحيث يمكن تنفيذها مباشرة:

1. ابدأ بالإجابة أو الإجراء التالي: الأمر أو المسار أو المقتطف أولاً.
2. رقّم العمل متعدد الخطوات، واجعل كل خطوة إجراءً واحدًا محددًا.
3. اختم بإجراء تالٍ واحد يمكن تنفيذه في أقل من دقيقتين.
4. أنهِ المشكلة الحالية قبل طرح مشكلة جديدة.
5. أعد توضيح التقدم في كل رد ("اكتملت الخطوة 3 من 5").
6. قدّم تقديرات زمنية بوحدات محددة، ولا تقل "قليلاً".
7. وضّح ما أصبح يعمل بعد إجراء أي تغيير.
8. عند حدوث خطأ، اذكر مكانه وسببه وطريقة إصلاحه بلا تهويل.
9. اجعل القوائم في حدود خمسة عناصر.
10. لا مقدمات، ولا إعادة تلخيص، ولا عبارات ختامية.

الاستثناءات: اشرح بالتفصيل عندما يُطلب منك ذلك. اطلب التأكيد قبل الإجراءات المدمرة. بعد ثلاث محاولات إصلاح فاشلة، توقّف وحدد الافتراض المشكوك فيه. إذا كان الطلب ملتبسًا، فاطرح سؤالاً قصيرًا واحدًا.
```

</details>

<details>
<summary><strong>AstronClaw (custom skill)</strong></summary>

يدعم AstronClaw استيراد ملف Markdown كمهارة مخصصة. تستخدم هذه الطريقة
ملف `SKILL.md` الحالي؛ راجع [دليل المهارات الرسمي](https://github.com/iflytek/astronclaw-tutorial/blob/main/docs/guide/astronclaw/skills.md)
للتحكم في التحميل والإدارة.

يتبع هذا الإجراء وثائق AstronClaw، لكنه لم يُختبر مع
هذه المهارة. تحقق من التعليمات المصدرة قبل تمكينها.

### تثبيت

1. قم بتنزيل [SKILL.md](https://raw.githubusercontent.com/banavasi/ferret/main/skills/ferret/SKILL.md) الأساسي واحفظه باسم `SKILL.md`. قم بمراجعة محتوياته قبل التحميل.
2. في AstronClaw، افتح **我的技能 (مهاراتي)**، واختر **新建 (جديد)**، وقم بتحميل ملف `.md`.
3. تأكد من تسمية المهارة المستوردة `ferret`. استخدم **启用/禁用 (تمكين/تعطيل)** للتحكم في مدى توفرها.

لا يلزم سوى ملف المهارة بصيغة Markdown. يؤدي التحميل إلى إرسال هذا الملف إلى AstronClaw؛
لا تُعدّ ملفات بيان المكوّن الإضافي وخطافاته في المستودع جزءًا من هذا الإعداد.

### التحقق والتنشيط

تأكد من ظهور `ferret` في **مهاراتي**. استخدم **下载 (تنزيل)** لمراجعة
التعليمات المستوردة مقابل المهارة الأصلية، ثم فعّلها وجرّب:

```text
Use the ferret skill for this conversation. Explain how to create an empty Git repository in a new folder.
```

تأكد من أن الرد يبدأ بالإجراء ويُرقّم الخطوات. هذا فحص يدوي للمهارة المستوردة؛
فنجاح عملية التحميل وحده لا يثبت أن قواعد الاستجابة الخاصة بها مطبَّقة فعليًا.

### مذكرة التنشيط

يدعم AstronClaw كلاً من الطلبات الصريحة واستدعاء المهارات تلقائيًا.
لا يحدد دليله ما إذا كان يحترم `disable-model-invocation: true` أم لا،
لذا استخدم **تعطيل** عندما لا تريد أن تكون المهارة متاحة. ليست هناك حاجة
للاعتماد على أمر يبدأ بشرطة مائلة `/ferret`.

تطلب المهارة من المساعد الحفاظ على أسلوب المحادثة حتى
تقول `normal mode` أو `normal mode`. لا تغيّر هذه التعليمات حالة التفعيل في المنصة؛ عطّل المهارة وابدأ
محادثة جديدة لبدء جلسة من دونها.

### تحديث

قم بتنزيل أحدث إصدار من ملف `SKILL.md` الأساسي. إذا قمت بتخصيص النسخة المستوردة،
استخدم **下载 (تنزيل)** للاحتفاظ بنسخة احتياطية أولاً. للحصول على بديل نظيف، احذف
إدخال `ferret` القديم، وكرر عملية الاستيراد، وقم بتشغيل مطالبة التحقق
في محادثة جديدة.

### إلغاء التثبيت

في **مهاراتي**، حدد `ferret` واختر **删除 (حذف)**، ثم ابدأ
محادثة جديدة. للاحتفاظ بالنسخة المستوردة لوقت لاحق، اختر **تعطيل** بدلاً من ذلك.

</details>

<details>
<summary><strong>Claude Code</strong></summary>

### تثبيت

```bash
claude plugin marketplace add banavasi/ferret
claude plugin install ferret@ferret
```

اكتب `/ferret`.

### تحقق

```bash
claude plugin list
```

### تحديث

```bash
claude plugin marketplace update ferret
claude plugin update ferret@ferret
```

### إلغاء التثبيت

```bash
claude plugin uninstall ferret
claude plugin marketplace remove ferret
```

أو أبقِه مثبتًا وأوقف تشغيله: `claude plugin disable ferret`.

### تشغيل دائمًا (اختياري)

يقوم الخطاف `SessionStart` بتحميل مجموعة القواعد الكاملة في بداية كل جلسة، ولا حاجة إلى `/ferret`:

```bash
touch ~/.claude/.ferret-always
```

إذا كنت تستخدم دليل تكوين Claude مخصصًا، فقم بإنشاء العلامة هناك بدلاً من ذلك:

```bash
touch "$CLAUDE_CONFIG_DIR/.ferret-always"
```

للعودة إلى التفعيل عند الطلب:

```bash
rm ~/.claude/.ferret-always
```

يتم تشغيل الخطاف فقط عند وجود ملف العلامة، لذا فإن تثبيت المكوّن الإضافي لا يغير شيئًا من تلقاء نفسه. لا يزال "إيقاف وضع adhd" يقوم بإيقاف تشغيله للجلسة الحالية.

</details>


<details>
<summary><strong>Codex</strong></summary>

### تثبيت

```bash
codex plugin marketplace add banavasi/ferret --ref main
codex plugin add ferret@ferret
```

قم باستدعاء المهارة بشكل صريح عن طريق كتابة `$ferret`. لن يفعّلها Codex تلقائيًا.

### تحقق

```bash
codex plugin list
```

### تحديث

```bash
codex plugin marketplace upgrade ferret
codex plugin remove ferret
codex plugin add ferret@ferret
```

### إلغاء التثبيت

```bash
codex plugin remove ferret
codex plugin marketplace remove ferret
```

### تشغيل دائمًا (اختياري)

أضف إلى `~/.codex/AGENTS.md`:

```markdown
## أسلوب الإجابة

القارئ مصاب باضطراب فرط الحركة وتشتت الانتباه. صُغ كل إجابة بحيث يمكن تنفيذها مباشرة:

1. ابدأ بالإجابة أو الإجراء التالي: الأمر أو المسار أو المقتطف أولاً.
2. رقّم العمل متعدد الخطوات، واجعل كل خطوة إجراءً واحدًا محددًا.
3. اختم بإجراء تالٍ واحد يمكن تنفيذه في أقل من دقيقتين.
4. أنهِ المشكلة الحالية قبل طرح مشكلة جديدة.
5. أعد توضيح التقدم في كل رد ("اكتملت الخطوة 3 من 5").
6. قدّم تقديرات زمنية بوحدات محددة، ولا تقل "قليلاً".
7. وضّح ما أصبح يعمل بعد إجراء أي تغيير.
8. عند حدوث خطأ، اذكر مكانه وسببه وطريقة إصلاحه بلا تهويل.
9. اجعل القوائم في حدود خمسة عناصر.
10. لا مقدمات، ولا إعادة تلخيص، ولا عبارات ختامية.

الاستثناءات: اشرح بالتفصيل عندما يُطلب منك ذلك. اطلب التأكيد قبل الإجراءات المدمرة. بعد ثلاث محاولات إصلاح فاشلة، توقّف وحدد الافتراض المشكوك فيه. إذا كان الطلب ملتبسًا، فاطرح سؤالاً قصيرًا واحدًا.
```

</details>

<details>
<summary><strong>Grok (<code>grok</code>)</strong></summary>

يحمّل Grok ملفات المكوّن الإضافي والمهارة الموجودة أصلاً في المستودع؛ لا حاجة إلى بيان Grok منفصل. ثبّته مباشرة من GitHub، فعّل المكوّن الإضافي، ثم استدعِ المهارة. هناك خطوتان خاصتان بـ Grok وحده: `--trust` (تبقى الخطافات والمهارات معطّلة من دونها) و`grok plugin enable` (تبقى المكوّنات الإضافية متوقفة حتى يتم تفعيلها).

### تثبيت

```bash
grok plugin install banavasi/ferret --trust
grok plugin enable ferret
```

ابدأ جلسة Grok جديدة واكتب `/ferret`. يحترم Grok `disable-model-invocation: true`، لذا لا يُطبَّق شيء حتى تستدعي المهارة أو تُفعّل التشغيل الدائم.

### تحقق

```bash
grok plugin list
grok plugin details ferret
```

تأكد من إدراج `ferret`، وأنه مُفعَّل، وأنه يظهر مع مهارة وخطافات.

### تحديث

```bash
grok plugin update ferret
```

### إلغاء التثبيت

```bash
grok plugin uninstall ferret --confirm
```

أو أبقِه مثبتًا وأوقف تشغيله: `grok plugin disable ferret`.

### تشغيل دائمًا (اختياري)

أضف الكتلة إلى `~/.grok/AGENTS.md`، أو ضعها في `~/.grok/rules/ferret.md` (يحمّل Grok كليهما عند بدء الجلسة):

```markdown
## أسلوب الإجابة

القارئ مصاب باضطراب فرط الحركة وتشتت الانتباه. صُغ كل إجابة بحيث يمكن تنفيذها مباشرة:

1. ابدأ بالإجابة أو الإجراء التالي: الأمر أو المسار أو المقتطف أولاً.
2. رقّم العمل متعدد الخطوات، واجعل كل خطوة إجراءً واحدًا محددًا.
3. اختم بإجراء تالٍ واحد يمكن تنفيذه في أقل من دقيقتين.
4. أنهِ المشكلة الحالية قبل طرح مشكلة جديدة.
5. أعد توضيح التقدم في كل رد ("اكتملت الخطوة 3 من 5").
6. قدّم تقديرات زمنية بوحدات محددة، ولا تقل "قليلاً".
7. وضّح ما أصبح يعمل بعد إجراء أي تغيير.
8. عند حدوث خطأ، اذكر مكانه وسببه وطريقة إصلاحه بلا تهويل.
9. اجعل القوائم في حدود خمسة عناصر.
10. لا مقدمات، ولا إعادة تلخيص، ولا عبارات ختامية.

الاستثناءات: اشرح بالتفصيل عندما يُطلب منك ذلك. اطلب التأكيد قبل الإجراءات المدمرة. بعد ثلاث محاولات إصلاح فاشلة، توقّف وحدد الافتراض المشكوك فيه. إذا كان الطلب ملتبسًا، فاطرح سؤالاً قصيرًا واحدًا.
```

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

لا يوجد لدى Gemini CLI سوق للمكونات الإضافية، لذلك هناك طريقان أصليان: **أمر مخصص** (اختياري، ويبقى معطلاً حتى تستدعيه) أو **امتداد** (يعمل دائمًا بمجرد تثبيته). يتطابق مسار الأمر مع الوضع الافتراضي لهذه المهارة؛ اختره إلا إذا كنت تريد القواعد في كل جلسة.

### التثبيت (الأمر، تفعيل اختياري)

```bash
mkdir -p ~/.gemini/commands
curl -fsSL https://raw.githubusercontent.com/banavasi/ferret/main/skills/ferret/agents/gemini.toml \
  -o ~/.gemini/commands/ferret.toml
```

ابدأ جلسة جديدة، اكتب `/ferret`. يبقى في تلك الجلسة.

### التثبيت (امتداد، تشغيل دائم)

```bash
gemini extensions install https://github.com/banavasi/ferret
```

يحمّل الامتداد ملف `GEMINI.md`، الذي يستورد المهارة الكاملة، وبالتالي يتم تطبيق القواعد من الرسالة الأولى. يجب تثبيت `git`.

### تحقق

```bash
gemini extensions list          # طريقة الامتداد
ls ~/.gemini/commands           # طريقة الأمر: ملف ferret.toml موجود
```

أو اكتب `/` في الجلسة وتأكد من إدراج `ferret`.

### تحديث

```bash
gemini extensions update ferret    # طريقة الامتداد
# طريقة الأمر: أعد تشغيل أمر curl أعلاه
```

### إلغاء التثبيت

```bash
gemini extensions uninstall ferret    # طريقة الامتداد
rm ~/.gemini/commands/ferret.toml     # طريقة الأمر
```

</details>

<details>
<summary><strong>GitHub Copilot (VS Code and Copilot CLI)</strong></summary>

يقرأ Copilot مهارات الوكيل أصلاً: نفس `SKILL.md`، بدون تحويل. فهو يقوم بمسح `.github/skills/`، و`.claude/skills/`، و`.agents/skills/` في المشروع، و`~/.copilot/skills/`، و`~/.claude/skills/`، و`~/.agents/skills/` عالميًا.

### تثبيت

```bash
npx skills add banavasi/ferret -a github-copilot        # هذا المشروع
npx skills add banavasi/ferret -a github-copilot -g     # جميع المشاريع
```

بدون واجهة سطر الأوامر (CLI)، انسخ مجلد المهارات إلى أي دليل يقوم Copilot بمسحه:

```bash
git clone https://github.com/banavasi/ferret
mkdir -p ~/.copilot/skills
cp -R ferret/skills/ferret ~/.copilot/skills/
```

### تحقق

اكتب `/` في مدخلات الدردشة وأكد ظهور `ferret`. أو:

```bash
npx skills list
npx skills ls -g    # إذا ثُبّتت عالميًا
```

### تحديث

```bash
npx skills update ferret
```

أو أعد نسخ المجلد بعد `git pull`.

### إلغاء التثبيت

```bash
npx skills remove ferret
```

أو احذف المجلد `ferret` من دليل المهارات الذي نسخته إليه.

### مذكرة التنشيط

يحترم Copilot `disable-model-invocation`: لا شيء ينطبق حتى تقوم باستدعاء المهارة، مثل Claude Code (تم اختباره في [#60](https://github.com/banavasi/ferret/pull/60)).

### تشغيل دائمًا (اختياري)

أضف الكتلة أدناه إلى `.github/copilot-instructions.md` في المشروع (يقرأها برنامج Copilot في كل محادثة):

```markdown
## أسلوب الإجابة

القارئ مصاب باضطراب فرط الحركة وتشتت الانتباه. صُغ كل إجابة بحيث يمكن تنفيذها مباشرة:

1. ابدأ بالإجابة أو الإجراء التالي: الأمر أو المسار أو المقتطف أولاً.
2. رقّم العمل متعدد الخطوات، واجعل كل خطوة إجراءً واحدًا محددًا.
3. اختم بإجراء تالٍ واحد يمكن تنفيذه في أقل من دقيقتين.
4. أنهِ المشكلة الحالية قبل طرح مشكلة جديدة.
5. أعد توضيح التقدم في كل رد ("اكتملت الخطوة 3 من 5").
6. قدّم تقديرات زمنية بوحدات محددة، ولا تقل "قليلاً".
7. وضّح ما أصبح يعمل بعد إجراء أي تغيير.
8. عند حدوث خطأ، اذكر مكانه وسببه وطريقة إصلاحه بلا تهويل.
9. اجعل القوائم في حدود خمسة عناصر.
10. لا مقدمات، ولا إعادة تلخيص، ولا عبارات ختامية.

الاستثناءات: اشرح بالتفصيل عندما يُطلب منك ذلك. اطلب التأكيد قبل الإجراءات المدمرة. بعد ثلاث محاولات إصلاح فاشلة، توقّف وحدد الافتراض المشكوك فيه. إذا كان الطلب ملتبسًا، فاطرح سؤالاً قصيرًا واحدًا.
```

</details>


<details>
<summary><strong>Hermes</strong></summary>

### تثبيت

```bash
hermes skills install banavasi/ferret/skills/ferret
```

اكتب `/ferret`. يتم تثبيت المهارة في `~/.hermes/skills/` ويتم عرضها كأمر يبدأ بشرطة مائلة في بداية الجلسة التالية.

هل تفضل التصفح أولا؟ أضف هذا المستودع كمصدر للمهارات (tap)، ثم ابحث وثبّت:

```bash
hermes skills tap add banavasi/ferret
hermes skills search ferret
hermes skills install banavasi/ferret/skills/ferret
```

### تحقق

```bash
hermes skills list
```

### تحديث

```bash
hermes skills update ferret
```

### إلغاء التثبيت

```bash
hermes skills uninstall ferret
```

ولإزالة مصدر المهارات أيضًا: `hermes skills tap remove banavasi/ferret`.

### تشغيل دائمًا (اختياري)

أضف إلى `AGENTS.md` في دليل العمل الخاص بك (يقوم Hermes بتحميله لكل دليل عمل)، أو إلى شخصيتك `SOUL.md` لكل جلسة:

```markdown
## أسلوب الإجابة

القارئ مصاب باضطراب فرط الحركة وتشتت الانتباه. صُغ كل إجابة بحيث يمكن تنفيذها مباشرة:

1. ابدأ بالإجابة أو الإجراء التالي: الأمر أو المسار أو المقتطف أولاً.
2. رقّم العمل متعدد الخطوات، واجعل كل خطوة إجراءً واحدًا محددًا.
3. اختم بإجراء تالٍ واحد يمكن تنفيذه في أقل من دقيقتين.
4. أنهِ المشكلة الحالية قبل طرح مشكلة جديدة.
5. أعد توضيح التقدم في كل رد ("اكتملت الخطوة 3 من 5").
6. قدّم تقديرات زمنية بوحدات محددة، ولا تقل "قليلاً".
7. وضّح ما أصبح يعمل بعد إجراء أي تغيير.
8. عند حدوث خطأ، اذكر مكانه وسببه وطريقة إصلاحه بلا تهويل.
9. اجعل القوائم في حدود خمسة عناصر.
10. لا مقدمات، ولا إعادة تلخيص، ولا عبارات ختامية.

الاستثناءات: اشرح بالتفصيل عندما يُطلب منك ذلك. اطلب التأكيد قبل الإجراءات المدمرة. بعد ثلاث محاولات إصلاح فاشلة، توقّف وحدد الافتراض المشكوك فيه. إذا كان الطلب ملتبسًا، فاطرح سؤالاً قصيرًا واحدًا.
```

</details>

<details>
<summary><strong>Kimi Code CLI</strong></summary>

### تثبيت

ابدأ جلسة Kimi Code، ثم:

1. قم بتشغيل `/plugins`.
2. اختر **مخصص**.
3. الصق `https://github.com/banavasi/ferret` ثم اضغط على `Enter`.
4. اختر **الثقة والتثبيت**.

استخدم الأمر الذي يبدأ بشرطة مائلة `/skill:ferret` لاستدعاء المهارة بشكل صريح.

### تحديث

`/plugins` في جلسة Kimi Code، ضع المؤشر على **Ferret**، ثم اضغط على `R`.

### إلغاء التثبيت

`/plugins` في جلسة Kimi Code، ضع المؤشر على **Ferret**، ثم اضغط على `D`.


</details>

<details>
<summary><strong>OpenCode</strong></summary>

يدعم المكوّن الإضافي OpenCode V1 **1.18.29 وما بعده** وV2. يسجّل المهارة والأمر `/ferret` ويتيح وضع التشغيل الدائم اختياريًا. تحتاج إصدارات V1 الأقدم إلى التحديث أو استخدام المكوّن الإضافي من الإصدار السابق للمهارة.

### تثبيت

للاستخدام في جميع المشاريع:

```bash
git clone https://github.com/banavasi/ferret ~/.config/opencode/vendor/ferret
mkdir -p ~/.config/opencode/plugins
cat > ~/.config/opencode/plugins/ferret.js <<'EOF'
export { default } from '../vendor/ferret/.opencode/plugins/ferret.mjs';
EOF
```

للتثبيت الحالي على V1، احتفظ بإدخال `plugin` في `opencode.json`. إذا انتقلت إلى ملف التحميل أعلاه، فاحذف ذلك الإدخال.

ابدأ جلسة جديدة واكتب `/ferret`. تظل القواعد سارية حتى تقول `normal mode` أو `normal mode`.

#### المهارة والأمر فقط (دون تشغيل دائم)

بدلًا من ذلك، انسخ المهارة والأمر من المستودع إلى مجلدات OpenCode العامة:

```bash
mkdir -p ~/.config/opencode/skills/ferret ~/.config/opencode/commands
cp skills/ferret/SKILL.md ~/.config/opencode/skills/ferret/SKILL.md
cp .opencode/command/ferret.md ~/.config/opencode/commands/ferret.md
```

### تحقق

شغّل OpenCode، واكتب `/`، وتأكد من ظهور `ferret` في قائمة الأوامر.

### تحديث

```bash
git -C ~/.config/opencode/vendor/ferret pull
```

إذا استخدمت التثبيت بالنسخ، حدّث نسختك المحلية ثم انسخ الملفين مجددًا.

### إلغاء التثبيت

احذف `~/.config/opencode/plugins/ferret.js`. للتثبيت بالنسخ، احذف `~/.config/opencode/skills/ferret/` و`~/.config/opencode/commands/ferret.md`. لإعداد V1 الحالي، أزل إدخال `plugin` الخاص به.

### تشغيل دائم (اختياري)

يتطلب المكوّن الإضافي. يضيف إنشاء ملف العلامة مجموعة القواعد الكاملة إلى موجّه النظام في كل رد:

```bash
touch ~/.config/opencode/.ferret-always
```

يطلب `normal mode` أو `normal mode` من الوكيل العودة إلى نمط الرد المعتاد في الجلسة الحالية. احذف العلامة لإيقاف إضافة القواعد تلقائيًا:

```bash
rm ~/.config/opencode/.ferret-always
```

إذا كان `XDG_CONFIG_HOME` محددًا، فاستبدل `~/.config` في هذه المسارات بذلك المجلد.

</details>


<details>
<summary><strong>Pi</strong></summary>

يكتشف Pi هذا المستودع كحزمة أصلية: يوفر `extensions/` الوضع المستمر للجلسة ويُبقي `skills/` نقطة دخول مهارات الوكيل متاحة.

### تثبيت

```bash
pi install https://github.com/banavasi/ferret
```

ابدأ جلسة Pi جديدة. بدّل الإخراج المناسب لـ ADHD للجلسة الحالية:

```text
/ferret
```

يُظهر التذييل `● FERRET ON` أثناء تنشيط الوضع. شغّل الأمر مرة أخرى لتعطيله، أو حدّد الحالة صراحةً:

```text
/ferret on
/ferret off
normal mode
```

مثل خطاف Claude Code، يضيف الامتداد مجموعة القواعد إلى المحادثة مرة واحدة بدلاً من إعادة كتابة موجه النظام عند كل طلب، ويضيفها مرة أخرى إذا أزالتها عملية ضغط السياق.

يظل أمر مهارات الوكيل الحالي متاحًا كاسم مستعار:

```text
/skill:ferret
```

ابدأ جلسة Pi جديدة مع تمكين الوضع افتراضيًا:

```bash
pi --ferret
```

### تحقق

```bash
pi list
```

تأكد من إدراج حزمة GitHub، ثم اكتب `/ferret` وتأكد من ظهور `● FERRET ON` في التذييل.

### تحديث

```bash
pi update https://github.com/banavasi/ferret
```

أو قم بتحديث كل حزمة Pi غير المثبّتة بإصدار محدد باستخدام `pi update --extensions`.

### إلغاء التثبيت

```bash
pi remove https://github.com/banavasi/ferret
```

### تشغيل دائمًا (اختياري)

قم بإنشاء علامة في دليل تكوين وكيل Pi:

```bash
touch ~/.pi/agent/.ferret-always
```

يتحقق الامتداد من العلامة في كل جلسة جديدة أو مستأنفة أو متشعبة أو مُعاد تحميلها. تكون الأولوية للاختيار المحفوظ للجلسة الحالية على هذا الإعداد الافتراضي، لذا فإن `normal mode` يبقي تلك الجلسة معطلة.

للعودة إلى التفعيل عند الطلب:

```bash
rm ~/.pi/agent/.ferret-always
```

### ملف التكوين (اختياري)

قم بإنشاء `~/.pi/agent/ferret.json` في دليل تكوين وكيل Pi:

```json
{
  "alwaysOn": true,
  "hideStatus": true
}
```

- `alwaysOn`: ابدأ كل جلسة مع القواعد النشطة - مثل ملف العلامة `.ferret-always`، الذي لا يزال يعمل
- `hideStatus`: احتفظ بإدخال شريط الحالة `● FERRET ON` مخفيًا؛ لا تزال القواعد والأمر `/ferret` تعمل

يُقرأ الملف مرة واحدة عند بدء تشغيل الامتداد، لذا أعد تشغيل Pi بعد تغييره. تكون الأولوية للاختيار المحفوظ للجلسة الحالية على `alwaysOn`، لذا فإن `normal mode` يبقي تلك الجلسة معطلة.

إذا تم تعيين `PI_CODING_AGENT_DIR`، فضع `.ferret-always` في هذا الدليل بدلاً من ذلك. قم بتشغيل `/reload` أو ابدأ جلسة جديدة بعد تغيير العلامة.

</details>


<details>
<summary><strong>Oh My Pi (OMP)</strong></summary>

### تثبيت

```bash
omp plugin marketplace add banavasi/ferret
omp plugin install --scope user ferret@ferret
```

ابدأ جلسة OMP جديدة وقم بتشغيل `/ferret` لتبديل الوضع.

### تحديث

```bash
omp plugin marketplace update ferret
omp plugin upgrade --scope user ferret@ferret
```

### إلغاء التثبيت

```bash
omp plugin uninstall --scope user ferret@ferret
omp plugin marketplace remove ferret
```

</details>


<details>
<summary><strong>Qwen Code</strong></summary>

### تثبيت

```bash
qwen extensions install banavasi/ferret
```

يدعم Qwen Code اختصار GitHub ويثبّت المستودع كامتداد أصلي. يكتشف الامتداد المهارة تحت `skills/`.

اكتب `/ferret` لاستدعاء المهارة بشكل صريح. تثبيت الامتداد
لا يغير الإخراج حتى يتم استدعاء المهارة.

### تحقق

```bash
qwen extensions list
```

ثم ابدأ جلسة Qwen Code جديدة وقم بتشغيل:

```text
/skills
```

تأكد من ظهور `ferret` في القائمة.

### تحديث

```bash
qwen extensions update ferret
```

### إلغاء التثبيت

```bash
qwen extensions uninstall ferret
```

</details>

<details>
<summary><strong>Zed</strong></summary>

يقرأ وكيل Zed مهارات الوكيل أصلاً باستخدام نفس تنسيق SKILL.md دون تحويل. لاحظ أنه تم استبدال قواعد Zed القديمة بالمهارات جنبًا إلى جنب مع تعليمات AGENTS.md.

### تثبيت

في لوحة الوكيل، افتح مدير المهارات واختر **إنشاء مهارة من عنوان URL** (أيضًا في لوحة الأوامر باسم `agent: create skill from url`)، ثم الصق:

```
https://github.com/banavasi/ferret/blob/main/skills/ferret/SKILL.md
```

احفظها في نطاق **المستخدم** لجميع المشاريع، أو في نطاق **المشروع** لمشروع واحد. ثم اكتب `/ferret` في لوحة الوكيل.

تفضل نظام الملفات؟ استنسخ المستودع وضَع مجلد المهارات في دليل مهارات المستخدم الخاص بك:

```bash
git clone https://github.com/banavasi/ferret
mkdir -p ~/.agents/skills
cp -R ferret/skills/ferret ~/.agents/skills/
```

### تحقق

افتح مدير المهارات في لوحة الوكيل وتأكد من إدراج `ferret`. أو اكتب `/` وأكد ظهوره.

### تحديث

أعد الاستيراد من نفس عنوان URL (الكتابة فوق)، أو أعد نسخ المجلد بعد `git pull`.

### إلغاء التثبيت

قم بإزالة `ferret` من مدير المهارات، أو قم بحذف `~/.agents/skills/ferret`.

### تشغيل دائمًا (اختياري)

أضف إلى ملفك الشخصي `~/.config/zed/AGENTS.md`:

```markdown
## أسلوب الإجابة

القارئ مصاب باضطراب فرط الحركة وتشتت الانتباه. صُغ كل إجابة بحيث يمكن تنفيذها مباشرة:

1. ابدأ بالإجابة أو الإجراء التالي: الأمر أو المسار أو المقتطف أولاً.
2. رقّم العمل متعدد الخطوات، واجعل كل خطوة إجراءً واحدًا محددًا.
3. اختم بإجراء تالٍ واحد يمكن تنفيذه في أقل من دقيقتين.
4. أنهِ المشكلة الحالية قبل طرح مشكلة جديدة.
5. أعد توضيح التقدم في كل رد ("اكتملت الخطوة 3 من 5").
6. قدّم تقديرات زمنية بوحدات محددة، ولا تقل "قليلاً".
7. وضّح ما أصبح يعمل بعد إجراء أي تغيير.
8. عند حدوث خطأ، اذكر مكانه وسببه وطريقة إصلاحه بلا تهويل.
9. اجعل القوائم في حدود خمسة عناصر.
10. لا مقدمات، ولا إعادة تلخيص، ولا عبارات ختامية.

الاستثناءات: اشرح بالتفصيل عندما يُطلب منك ذلك. اطلب التأكيد قبل الإجراءات المدمرة. بعد ثلاث محاولات إصلاح فاشلة، توقّف وحدد الافتراض المشكوك فيه. إذا كان الطلب ملتبسًا، فاطرح سؤالاً قصيرًا واحدًا.
```

</details>

<details>
<summary><strong>Cursor, Amp, and any other agent-skills harness</strong></summary>

يعمل مع أي بيئة تدعم مهارات الوكيل. استبدل `<agent>` باسم وكيلك في الخيار `-a`.

### تثبيت

```bash
npx skills add banavasi/ferret                  # مساحة العمل هذه
npx skills add banavasi/ferret -g               # جميع المشاريع
npx skills add banavasi/ferret -a cursor -y     # وكيل واحد فقط
npx skills add banavasi/ferret -a opencode -y
```

في محادثة جديدة مع الوكيل، اكتب `/ferret`.

بدون واجهة سطر الأوامر (CLI)، انسخ مجلد المهارات إلى أي مسار يفحصه وكيلك:

```bash
git clone https://github.com/banavasi/ferret
mkdir -p ~/.cursor/skills     # استخدم .agents/skills مع OpenCode أو المسار الخاص بوكيلك
cp -R ferret/skills/ferret ~/.cursor/skills/
```

### تحقق

```bash
npx skills list
npx skills ls -g    # إذا ثُبّتت عالميًا
```

### تحديث

```bash
npx skills update ferret
npx skills update -g    # إذا ثُبّتت عالميًا
```

### إلغاء التثبيت

```bash
npx skills remove ferret
npx skills remove ferret -g    # إذا ثُبّتت عالميًا
```

### تشغيل دائمًا (اختياري)

الصق هذا في ملف القواعد الثابتة لوكيلك. في Cursor: **الإعدادات → القواعد → قواعد المستخدم**، أو قاعدة مشروع ضمن `.cursor/rules/` مع `alwaysApply: true`. وفي OpenCode: `~/.config/opencode/AGENTS.md`.

```markdown
## أسلوب الإجابة

القارئ مصاب باضطراب فرط الحركة وتشتت الانتباه. صُغ كل إجابة بحيث يمكن تنفيذها مباشرة:

1. ابدأ بالإجابة أو الإجراء التالي: الأمر أو المسار أو المقتطف أولاً.
2. رقّم العمل متعدد الخطوات، واجعل كل خطوة إجراءً واحدًا محددًا.
3. اختم بإجراء تالٍ واحد يمكن تنفيذه في أقل من دقيقتين.
4. أنهِ المشكلة الحالية قبل طرح مشكلة جديدة.
5. أعد توضيح التقدم في كل رد ("اكتملت الخطوة 3 من 5").
6. قدّم تقديرات زمنية بوحدات محددة، ولا تقل "قليلاً".
7. وضّح ما أصبح يعمل بعد إجراء أي تغيير.
8. عند حدوث خطأ، اذكر مكانه وسببه وطريقة إصلاحه بلا تهويل.
9. اجعل القوائم في حدود خمسة عناصر.
10. لا مقدمات، ولا إعادة تلخيص، ولا عبارات ختامية.

الاستثناءات: اشرح بالتفصيل عندما يُطلب منك ذلك. اطلب التأكيد قبل الإجراءات المدمرة. بعد ثلاث محاولات إصلاح فاشلة، توقّف وحدد الافتراض المشكوك فيه. إذا كان الطلب ملتبسًا، فاطرح سؤالاً قصيرًا واحدًا.
```
</details>


## كيف يعمل التنشيط

1. **تم التثبيت، ولم يتم استدعاؤه.** في Claude Code، وQwen Code، وCodex، وGrok، لا يحدث شيء حتى تقوم باستدعاء المهارة بشكل صريح. يحترم Claude Code وQwen Code وGrok `disable-model-invocation: true` في `SKILL.md`؛ ويحترم Codex `policy.allow_implicit_invocation: false` في `agents/openai.yaml`. قد تقوم الأدوات الأخرى بتحميل وصف كل مهارة عند بدء التشغيل، وقد تنشّط المهارة من تلقاء نفسها.
2. **أنت تستدعيه بشكل صريح.** اكتب `/ferret` في Claude Code أو Qwen Code أو Grok، أو `$ferret` في Codex. تبقى القواعد سارية لتلك الجلسة. يؤدي `normal mode` أو `normal mode` إلى تعطيل الوضع.
3. **أنشئ `~/.claude/.ferret-always`** (في Claude Code). يقوم الخطاف `SessionStart` بتحميل مجموعة القواعد الكاملة من الرسالة الأولى، في كل جلسة.
4. **أضف مقتطف التشغيل الدائم أعلاه** (Grok، وCodex، وأدوات أخرى). يقرأ Grok كلاً من `~/.grok/AGENTS.md` و`~/.grok/rules/*.md`. يحافظ هذا على القواعد الأساسية ضمن السياق المستمر لوكيلك.

في Claude Code، وQwen Code، وCodex، وGrok، لا يوجد حل وسط: إذا لم تُفعّله، فهو معطّل.

## استكشاف الأخطاء وإصلاحها

**`/ferret` ليس في وضع الإكمال التلقائي.** أعد تشغيل الوكيل. تتم قراءة فهرس المكوّن الإضافي عند بدء التشغيل. في Grok، شغّل أيضًا `grok plugin enable ferret` وتأكد من أن التثبيت استخدم `--trust`.

**علامة التشغيل الدائم ليس لها أي تأثير.** قم بتحديث المكوّن الإضافي (`claude plugin marketplace update ferret` ثم `claude plugin update ferret@ferret`) وأعد التشغيل. تتم قراءة الخطافات عند بدء التشغيل، ويتطلب ملف العلامة إصدارًا من المكوّن الإضافي يتضمن `hooks/hooks.json`. لا يقرأ Grok ملف `~/.claude/.ferret-always`؛ ضع كتلة التشغيل الدائم بدلاً من ذلك في `~/.grok/AGENTS.md` أو `~/.grok/rules/ferret.md`.

**فشل `claude plugin marketplace add`.** استخدم نموذج `owner/repo`. يجب أن يشير المسار المحلي إلى جذر المستودع، وليس إلى `.claude-plugin/`.

**`grok plugin install` لا يُحدث أي أثر ظاهر.** أضف `--trust`، ثم شغّل `grok plugin enable ferret`، ثم ابدأ جلسة جديدة. تبقى مكوّنات Grok الإضافية معطّلة وغير موثوقة حتى تتم هاتان الخطوتان.

**تم التثبيت ولكن الردود لا تزال تبدأ بمقدمة.** افتح جلسة جديدة. إذا استمرت الإجابات في مخالفة القواعد، فشدّد الصياغة في `skills/ferret/SKILL.md`.

**تريد قواعد مختلفة.** أنشئ نسخة متفرعة، وقم بتحرير `skills/ferret/SKILL.md`، ثم استبدل النسخة الأصلية بنسختك:

```bash
claude plugin uninstall ferret            # أزل النسخة الأصلية أولاً
claude plugin marketplace remove ferret   # النسخة المتفرعة والأصلية تحملان الاسم نفسه
claude plugin marketplace add <your-username>/ferret
claude plugin install ferret@ferret
```

أعد التشغيل، ثم أعد استدعاء `/ferret`.

**المهارة مفقودة بعد `npx skills add`.** ابدأ محادثة جديدة مع الوكيل. تتم فهرسة المهارات عند بداية الجلسة. تأكد من وجود المجلد في المسار الذي يفحصه وكيلك (`~/.cursor/skills/` لـ Cursor، `.agents/skills/` لـ OpenCode) وأن الحقل `name` في ترويسة الملف (frontmatter) يتطابق مع اسم المجلد.
