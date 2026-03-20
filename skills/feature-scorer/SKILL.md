# Skill Definition for Feature Scorer

## Name
Feature Scorer

## Trigger
Initiated when a new feature idea is proposed for evaluation.

## Model
GPT-4

## Context Inputs
- Feature idea description
- Historical data of previous feature scores
- Team's strategic goals

## System Prompt
Evaluate the proposed feature idea based on its impact, effort required, risk factors, and alignment with strategic goals. Assign a score from 1 to 10 for each category, providing a brief explanation for each score.

## Output Format
```
{
  "feature_idea": "[description of the feature idea]",
  "impact_score": [score out of 10],
  "effort_score": [score out of 10],
  "risk_score": [score out of 10],
  "strategic_alignment_score": [score out of 10],
  "explanations": {
    "impact": "[explanation of impact score]",
    "effort": "[explanation of effort score]",
    "risk": "[explanation of risk score]",
    "strategic_alignment": "[explanation of strategic alignment score]"
  }
}
```
