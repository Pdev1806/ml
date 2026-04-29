from textblob import TextBlob
import requests

def fetch_news(vendor_name):
    url = "https://newsapi.org/v2/everything"
    
    params = {
        "q": vendor_name,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5
    }

    headers = {
        "X-Api-Key": "6c9eb93-f6d8-4eab-ac12-4a8310562c4d"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return []

    data = response.json()

    articles = []
    for article in data.get("articles", []):
        title = article.get("title", "")
        description = article.get("description", "")
        content = (title + " " + description).strip()
        if content:
            articles.append(content)

    return articles

def calculate_news_risk(news_articles):
    negative_score = 0

    for article in news_articles:
        sentiment = TextBlob(article).sentiment.polarity
        if sentiment < 0:
            negative_score += abs(sentiment) * 100

    return min(negative_score, 100)

def calculate_sla_risk(breaches, max_breaches=10):
    return min((breaches / max_breaches) * 100, 100)

def calculate_overall_risk(cyber_score, financial_score, news_risk, sla_risk):
    risk_score = (
        0.3 * cyber_score +
        0.25 * financial_score +
        0.2 * news_risk +
        0.15 * sla_risk +
        0.1 * 0
    )
    return round(risk_score, 2)

def classify_risk(score):
    if score <= 30:
        return "Low Risk"
    elif score <= 60:
        return "Medium Risk"
    else:
        return "High Risk"

def detect_material_change(old_score, new_score, threshold=15):
    return (new_score - old_score) > threshold

def generate_explanation(cyber_score, financial_score, news_risk, sla_risk):
    reasons = []

    if cyber_score > 70:
        reasons.append("High cybersecurity exposure")
    if financial_score > 70:
        reasons.append("Weak financial indicators")
    if news_risk > 50:
        reasons.append("Significant negative news coverage")
    if sla_risk > 50:
        reasons.append("Frequent SLA breaches")

    if not reasons:
        return "No major risk drivers detected."

    return "Risk increased due to: " + ", ".join(reasons)

if __name__ == "__main__":
    vendor_name = "Netflix"

    cyber_risk = 65
    financial_risk = 55
    breaches = 3

    print("\nFetching latest news for:", vendor_name)
    news_articles = fetch_news(vendor_name)
    print("Fetched", len(news_articles), "articles")

    news_risk = calculate_news_risk(news_articles)
    sla_risk = calculate_sla_risk(breaches)

    old_risk_score = 40

    new_risk_score = calculate_overall_risk(
        cyber_risk,
        financial_risk,
        news_risk,
        sla_risk
    )

    risk_level = classify_risk(new_risk_score)
    alert_triggered = detect_material_change(old_risk_score, new_risk_score)
    explanation = generate_explanation(
        cyber_risk,
        financial_risk,
        news_risk,
        sla_risk
    )

    print("\n------ Vendor Risk Report ------")
    print("Vendor:", vendor_name)
    print("Cyber Risk:", cyber_risk)
    print("Financial Risk:", financial_risk)
    print("News Risk:", news_risk)
    print("SLA Risk:", sla_risk)
    print("Overall Risk Score:", new_risk_score)
    print("Risk Level:", risk_level)
    print("Material Risk Increase:", alert_triggered)
    print("Explanation:", explanation)