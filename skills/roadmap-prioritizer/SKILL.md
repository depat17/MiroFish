# Roadmap Prioritizer Skill

## Skill Description
The Roadmap Prioritizer skill is designed to optimize build sequences based on feature lists and timeline memory context. This skill can effectively analyze the available features, user needs, and time constraints to produce a prioritized roadmap for development teams.

## Functionality
1. **Input Processing:**
   - Accepts a list of features, each with associated priority levels, dependencies, and estimated development times.
   - Integrates memory context regarding previously developed features and timelines to avoid redundancy.

2. **Prioritization Algorithm:**
   - Utilizes a custom algorithm that factors in:
     - Feature importance and user demand.
     - Resource availability and team workload.
     - Any existing dependencies between features.

3. **Output Generation:**
   - Produces an optimized sequence of build tasks along with timelines assigned to each.
   - Provides feedback on potential blockers or resource needs.

## Use Cases
- Ideal for product managers and development teams looking to streamline their build processes.
- Assists in strategic planning cycles with respect to feature delivery and resource allocation.

## Example Usage
```python
features = [{'name': 'Feature A', 'priority': 1, 'time': 3}, {'name': 'Feature B', 'priority': 2, 'time': 5}]
optimized_sequence = roadmap_prioritizer(features)
```

## Conclusion
The Roadmap Prioritizer skill is essential for enhancing development efficiency and ensuring that teams focus on delivering the most impactful features first.