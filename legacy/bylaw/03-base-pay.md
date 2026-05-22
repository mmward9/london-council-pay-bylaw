## 2. Base pay

(a) This bylaw applies to the following offices:

{% for office in policy.applies_to -%}
- {{ office | replace('_', ' ') | title }}
{% endfor %}

(b) The base pay for each Affected office is as follows:

| Office | Base pay (CAD per year) |
|---|---|
| Councillor | {{ policy.base_pay.councillor_cad | currency }} |
| Mayor | {{ policy.base_pay.mayor_cad | currency }} |

(c) The base pay for the Deputy Mayor and the Budget Chair is the Councillor base pay set out in clause 2(b) plus any additional remuneration lawfully prescribed by Council for those positions.

(d) The figures in clause 2(b) correspond to the lawful remuneration in force at the start of the council term commencing November 17, 2026. {{ policy.base_pay.source }}.
