import pandas as pd

performance = pd.read_csv("data/07_scheme_performance.csv")

# Risk Mapping
risk_map = {
    "Low": ["Gilt", "Debt"],
    "Moderate": ["Large Cap", "Flexi Cap", "Hybrid"],
    "High": ["Mid Cap", "Small Cap"]
}

risk_appetite = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

selected_categories = risk_map.get(
    risk_appetite,
    []
)

filtered = performance[
    performance["category"].isin(
        selected_categories
    )
].copy()

filtered["sharpe_proxy"] = (
    filtered["return_3yr_pct"] / 10
)

recommendations = filtered.sort_values(
    "sharpe_proxy",
    ascending=False
).head(3)

print("\nTop 3 Recommended Funds:\n")

print(
    recommendations[
        [
            "scheme_name",
            "category",
            "return_3yr_pct"
        ]
    ]
)