import time
from app import retrieve_context, generate_concierge_reply, filter_hotels, hotels_df

TEST_CASES = [
    {"query": "Recommend a harbour view hotel in Tsim Sha Tsui", "expected_source": "01_HK_Hotels_Master_Database.csv", "type": "Recommendation"},
    {"query": "What is the Hong Kong Hotel Accommodation Tax rate in 2026?", "expected_source": "02_HK_Hotel_Tax_and_Fees_Policy_2026.md", "type": "Policy QA"},
    {"query": "Are free plastic toothbrushes provided in Hong Kong hotels?", "expected_source": "03_HK_Disposable_Plastic_Ban_Hotel_Guide.md", "type": "Regulation QA"},
    {"query": "Which hotels in Hong Kong allow dogs or pets?", "expected_source": "11_Pet_Friendly_Staycation_Guide_HK.md", "type": "Preference Filter"},
    {"query": "Hotels near Hong Kong Airport with free shuttle bus", "expected_source": "08_District_Guide_Airport_Lantau_Disneyland.md", "type": "Transit QA"},
    {"query": "Best budget hotel in Central under HK$700", "expected_source": "13_Budget_and_Boutique_Hotels_HK.md", "type": "Budget Query"},
    {"query": "Which hotel is owned by PolyU in Hung Hom?", "expected_source": "07_District_Guide_HungHom_MongKok.md", "type": "Domain Fact"},
    {"query": "What is the standard check-out time and late check-out fee?", "expected_source": "15_CheckIn_CheckOut_and_Cancellation_FAQ.md", "type": "FAQ QA"},
    {"query": "Recommend a hotel in Tokyo near Shinjuku", "expected_source": "GUARDRAIL", "type": "Out-of-Domain"},
    {"query": "Book a resort in Macau Cotai Strip", "expected_source": "GUARDRAIL", "type": "Out-of-Domain"},
]

if __name__ == "__main__":
    print("=== COMP4431 HarbourAI Evaluation Benchmark ===")
    hits = 0
    total_latency = 0.0
    matched = filter_hotels(hotels_df, 6000, ["All Districts"], False, False, False, False)

    for i, tc in enumerate(TEST_CASES, 1):
        chunks = retrieve_context(tc["query"], top_k=3)
        reply, latency, mode = generate_concierge_reply(tc["query"], chunks, matched, api_key="", model_name="gpt-4o-mini")
        total_latency += latency
        retrieved_sources = [c["source"] for c in chunks]
        if tc["expected_source"] == "GUARDRAIL":
            passed = "exclusively in Hong Kong" in reply
        else:
            passed = tc["expected_source"] in retrieved_sources
        hits += int(passed)
        print(f"[{i:02d}] ({tc['type']}) Pass={passed} | Latency={latency:.3f}s | TopSource={retrieved_sources[0]}")

    print(f"
Overall Retrieval & Guardrail Accuracy: {hits}/{len(TEST_CASES)} ({hits/len(TEST_CASES)*100:.1f}%)")
    print(f"Average Response Latency: {total_latency/len(TEST_CASES):.3f}s")
