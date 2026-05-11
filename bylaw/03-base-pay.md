## 2. Base pay

(a) This bylaw applies to the following offices:

{% for office in policy.applies_to -%}
- {{ office | replace('_', ' ') | title }}
{% endfor %}

(b) The base pay for each Affected office is as follows:

| Office | Base pay (CAD per year) |
|---|---|
| Councillor | {{ policy.base_pay.councillor_cad | currency }} |
| Deputy Mayor | {{ policy.base_pay.deputy_mayor_cad | currency }} |
| Budget Chair | {{ policy.base_pay.budget_chair_cad | currency }} |
| Mayor | {{ policy.base_pay.mayor_cad | currency }} |

(c) These figures correspond to the lawful remuneration in force at the start of the council term commencing November 17, 2026. {{ policy.base_pay.source }}.
