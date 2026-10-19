# Rafeeq Mini — Advanced Agentic AI Systems Engineering
 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Maitha-t/rafeeq-mini-Maitha-Advanced-Agentic-AI-Systems-Engineering/blob/main/Rafeeq_mini.ipynb)
> A capstone project completed as part of the **Rafeeq Mini** program, delivered by **SDAIA Academy** — a 3-day, on-site, 18-hour intensive training program.

## Project scenario · سيناريو المشروع

A customer contacts the fictional delivery company **Tawseel** in Arabic or English to ask about an order or request a refund. Rafeeq detects the intent and order ID, verifies ownership through a scoped tool, retrieves only the active policy, delegates to the correct specialist, and records a redacted trace. Refunds require a delay greater than two days; amounts above SAR 500 pause for explicit human approval. Re-running a write remains safe through deterministic idempotency.

يتواصل عميل مع شركة التوصيل الافتراضية **توصيل** بالعربية أو الإنجليزية للسؤال عن طلب أو طلب استرداد. يحدد رفيق النية ورقم الطلب، ويتحقق من الملكية عبر أداة مقيّدة، ويسترجع السياسة السارية فقط، ويفوض المهمة للوكيل المتخصص، ويسجل أثرًا منقحًا. يشترط الاسترداد تأخرًا يزيد على يومين، وتتوقف المبالغ الأعلى من 500 ريال حتى تصدر موافقة بشرية صريحة. وتظل إعادة خلية الكتابة آمنة بفضل مفتاح منع التكرار الحتمي.

```mermaid
flowchart TB
    A["Bilingual request · طلب ثنائي اللغة"] --> B["Input guard · حارس المدخل"]
    B --> C["Thin supervisor · المنسق الخفيف"]
    C --> D["OrdersAgent"]
    C --> E["RefundAgent"]
    D --> F["MCP tools + scoped data · أدوات وبيانات مقيّدة"]
    E --> G["Policy + approval · السياسة والموافقة"]
    G --> F
    F --> H["Redacted trace + evidence · أثر منقح وأدلة"]
```
.
## Public Release Scorecard · بطاقة تقييم الإصدار العام
 
![Rafeeq Mini Public Release Scorecard](reports/monitoring_dashboard.png)
 
All three release gates — **Functional**, **Security**, and **Trace** — passed at a 100% rate.
 
اجتازت جميع بوابات الإصدار الثلاث — **الوظيفية**، **الأمنية**، و**التتبع** — بنسبة نجاح 100%.
## How to Run
 
1. Clone the repository:
```bash
   git clone https://github.com/Maitha-t/rafeeq-mini-Maitha-Advanced-Agentic-AI-Systems-Engineering.git
```
2. Open `Rafeeq-mini.ipynb` in Google Colab or Jupyter Notebook.
3. Run all cells sequentially to reproduce the full workflow, including the final security review and export steps.



## Training-program attribution
This project was completed for the **Rafeeq Mini**, delivered by **SDAIA Academy**, a three-day, on-site, 18-hour program. Session: September 2026.
 
All thanks to the greatest trainer: [**Meaad Al-Marri**](https://github.com/almiyead-rgb)
 
Training-program reference: [SDAIA Academy on GitHub](https://github.com/SDAIAAcademy)
