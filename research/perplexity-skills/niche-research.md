---
name: niche-research
description: Surface the 20 most relevant stories, trends, and discussions in the Indian organic food space from the last 7 days. Use whenever asked "what's trending", "research this week", "what's happening in organic food India", or when a brand name is dropped with a question about current conversations around it.
---

# Niche Research — Indian Organic Food

## Auto-start on load
Go straight to Step 1. No preamble.

## Step 1. Get the niche focus

Ask: What do you want researched? Options:
- All 5 brands — broad Indian organic food landscape
- Caveman Organic — millet, cookies, Gen Z snacking
- Health Fields — teas, honey, Ayurvedic wellness
- Pusht Organic — farm staples, cold-pressed oils, pulses
- greendipz — cooking sauces, gravies, Indo-Chinese cuisine
- Biomart — organic marketplace, multi-category

Or a specific topic/occasion the user types.

## Step 2. Search across 5 dimensions

Run searches across all of the following. Only include findings from the last 7 days unless the user says otherwise.

### 2a. Consumer Conversations
Search: "[niche] India Reddit", "[niche] India review", "[product category] India 2026"
Extract: what real consumers are saying, complaints, praise, questions being asked

### 2b. Brand & Competitor Moves
Search: "[competitor handles] Instagram campaign", "[brand] India launch 2026", "[category] brand India news"
Tracked competitors: @slurrpfarm, @thewholetruthfoods, @twobrothersorganicfarmsindia, @organicindiaofficial, @vahdamindia, @chingssecret, @veeba_in, @wingreensfarms, @yogabars.in, @earlyfoods
Extract: new campaigns, product launches, content formats being used

### 2c. Regulatory & Transparency News
Search: "FSSAI 2026", "Label Padhega India", "organic certification India news", "food labelling India"
Extract: any new guidelines, controversies, or transparency campaigns

### 2d. Festival & Occasion Angles
Search: "[upcoming Indian festival/occasion] food brand campaign", "[occasion] organic food India"
Extract: what angles brands are using, what's oversaturated, what's open

### 2e. Hook & Format Patterns
Search: "Instagram reels India food trending", "[category] reel hook India", "viral food content India 2026"
Extract: what opening lines, formats, and angles are gaining traction

## Step 3. Synthesise into a research table

Output a markdown table:

| Finding | Source | Brand Relevance | Signal Strength | Content Angle Opportunity |
|---------|--------|----------------|-----------------|--------------------------|

Signal Strength: High / Medium / Low based on how many sources confirm it.
Brand Relevance: Which of the 5 brands this applies to.
Content Angle Opportunity: One sentence on how to use this finding in a post.

## Step 4. Flag the top 3 actionable findings

After the table, list the 3 highest-signal findings in plain language with a recommended next action for each.

## Rules
- Never invent links, quotes, or dates
- Only include findings verifiable from search results
- Always note which brand each finding is most relevant to
- If fewer than 10 findings pass the 7-day filter, say so rather than padding with weak items
- Research only — no captions, no hooks, no copy
