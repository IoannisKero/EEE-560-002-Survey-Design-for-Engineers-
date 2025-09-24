import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter


# ========================================================================================================================
# STEP 1: Commuting Frequency Across Different Semesters
# ========================================================================================================================

# Data
data = {
    'Commute Days': ['0 days', '1–2 days', '3–4 days', '5–6 days', '7 days'],
    'Fall (%)':   [0, 0, 27.27, 72.73, 0],
    'Spring (%)': [9.09, 9.09, 9.09, 63.64, 0],
    'Summer (%)': [18.18, 27.27, 27.27, 27.27, 0]
}

import pandas as pd, numpy as np, matplotlib.pyplot as plt
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#2E86AB', '#A23B72', '#F18F01']
x = np.arange(len(df['Commute Days']))
width = 0.25

bars1 = ax.bar(x - width, df['Fall (%)'],   width, label='Fall',   color=colors[0], alpha=0.8)
bars2 = ax.bar(x,           df['Spring (%)'], width, label='Spring', color=colors[1], alpha=0.8)
bars3 = ax.bar(x + width, df['Summer (%)'], width, label='Summer', color=colors[2], alpha=0.8)

ax.set_xlabel('Commute Days', fontsize=18, fontweight='bold')
ax.set_ylabel('Percentage (%)', fontsize=18, fontweight='bold')
ax.set_title('Commuting Frequency Across Different Semesters', fontsize=20, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(df['Commute Days'], fontsize=16, fontweight='bold')
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:.0f}%'))
plt.yticks(fontsize=16)
ax.legend(title="Season", fontsize=16, title_fontsize=16)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Same y-scale (0–100) for consistency with other plots
ax.set_ylim(0, 100)

def add_value_labels(bars):
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2., h + 1.0,
                    f'{h:.1f}%', ha='center', va='bottom',
                    fontsize=14, fontweight='bold')

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)

plt.tight_layout()
plt.savefig('commuting_frequency_plot.png', dpi=300, bbox_inches='tight')
plt.show()


# ========================================================================================================================
# STEP 2: Mode of transportation - Seasonal Commuting Patterns
# ========================================================================================================================

# Data from the updated commuting modes table

data2 = {
    'Semester': ['Fall', 'Spring', 'Summer'],
    'Walking (%)':                  [54.55, 0.00, 9.09],
    'Bike/Scooter/Skateboard (%)':  [0.00, 9.09, 18.18],
    'Bus/Shuttle (%)':              [27.27, 18.18, 0.00],
    'Private Car (%)':              [72.73, 9.09, 0.00]
}
df2 = pd.DataFrame(data2)

fig, ax = plt.subplots(figsize=(14, 8))
colors2 = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']

x = np.arange(len(df2['Semester']))
width = 0.2

b1 = ax.bar(x - 1.5*width, df2['Walking (%)'],                 width, label='Walking',                 color=colors2[0], alpha=0.8)
b2 = ax.bar(x - 0.5*width, df2['Bike/Scooter/Skateboard (%)'], width, label='Bike/Scooter/Skateboard', color=colors2[1], alpha=0.8)
b3 = ax.bar(x + 0.5*width, df2['Bus/Shuttle (%)'],             width, label='Bus/Shuttle',             color=colors2[2], alpha=0.8)
b4 = ax.bar(x + 1.5*width, df2['Private Car (%)'],             width, label='Private Car',             color=colors2[3], alpha=0.8)

ax.set_xlabel('Semesters', fontsize=18, fontweight='bold')
ax.set_ylabel('Percentage (%)', fontsize=18, fontweight='bold')
ax.set_title('Mode of Transport - Seasonal Commuting Patterns', fontsize=20, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(df2['Semester'], fontsize=16, fontweight='bold')
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:.0f}%'))
plt.yticks(fontsize=16)
ax.legend(fontsize=16, title="Mode of Transport", title_fontsize=16, loc='upper right')
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Same y-scale (0–100)
ax.set_ylim(0, 100)

def add_labels(bars):
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2., h + 1.0,
                    f'{h:.1f}%', ha='center', va='bottom',
                    fontsize=14, fontweight='bold')

for bars in (b1, b2, b3, b4):
    add_labels(bars)

plt.tight_layout()
plt.savefig('commuting_modes_updated_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# ========================================================================================================================
# STEP 3: Mean Weekly Commuting Days by Mode & Season
# ========================================================================================================================


data = {
    "Walking": {
        "Fall":   [0,5.5,0,0,0,5.5,5.5,0,0,5.5,3.5],
        "Spring": [0,5.5,0,0,0,5.5,5.5,0,0,1.5,3.5],
        "Summer": [0,0,1.5,0,0,5.5,5.5,0,0,3.5,3.5]
    },
    "Bike": {
        "Fall":   [0,0,1.5,0,0,5.5,0,0,0,3.5,3.5],
        "Spring": [0,0,0,0,0,5.5,0,0,0,3.5,3.5],
        "Summer": [0,0,3.5,0,0,5.5,0,0,0,7,3.5]
    },
    "Bus": {
        "Fall":   [0,1.5,3.5,0,1.5,5.5,0,0,3.5,7,3.5],
        "Spring": [0,1.5,7,0,1.5,0,0,0,3.5,3.5,3.5],
        "Summer": [0,0,0,0,1.5,0,0,0,5.5,7,3.5]
    },
    "Car": {
        "Fall":   [5.5,0,0,5.5,5.5,5.5,5.5,0,5.5,0,3.5],
        "Spring": [5.5,0,1.5,5.5,5.5,5.5,5.5,0,5.5,0,3.5],
        "Summer": [3.5,0,0,3.5,5.5,3.5,0,0,5.5,0,3.5]
    }
}

# Calculate mean values for each mode in each semester
semesters = ['Fall', 'Spring', 'Summer']
modes = ['Walking', 'Bike', 'Bus', 'Car']

# Create a matrix to store mean values
mean_data = {}
for semester in semesters:
    mean_data[semester] = {}
    for mode in modes:
        mean_data[semester][mode] = np.mean(data[mode][semester])

# Convert to DataFrame for easier plotting
df_means = pd.DataFrame(mean_data)

print("Mean commuting days per week by mode and semester:")
print(df_means.round(2))

# =======================
# Create the plot
# =======================

fig, ax = plt.subplots(figsize=(12, 8))

# Define colors for each commuting mode
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']

x = np.arange(len(semesters))  # Fall, Spring, Summer
width = 0.2

# Plot bars
bars1 = ax.bar(x - 1.5*width, df_means.loc['Walking'], width, label='Walking', color=colors[0], alpha=0.8)
bars2 = ax.bar(x - 0.5*width, df_means.loc['Bike'], width, label='Bike', color=colors[1], alpha=0.8)
bars3 = ax.bar(x + 0.5*width, df_means.loc['Bus'], width, label='Bus', color=colors[2], alpha=0.8)
bars4 = ax.bar(x + 1.5*width, df_means.loc['Car'], width, label='Car', color=colors[3], alpha=0.8)

# Customize axes
ax.set_xlabel('Semesters', fontsize=18, fontweight='bold')
ax.set_ylabel('Mean Days/Week', fontsize=18, fontweight='bold')
ax.set_title('Mean Weekly Commuting Days by Mode & Season', fontsize=20, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(semesters, fontsize=16, fontweight='bold')
plt.yticks(fontsize=16)

# Legend
ax.legend(fontsize=16, title="Mode of Transport", title_fontsize=16, loc='upper right')

# Grid + Y limit
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_ylim(0, 7)  # consistent with max days/week

# Add value labels
def add_value_labels(bars):
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2., h + 0.1,
                   f'{h:.1f}', ha='center', va='bottom',
                   fontsize=14, fontweight='bold')

for b in (bars1, bars2, bars3, bars4):
    add_value_labels(b)

# Save before show
plt.tight_layout()
plt.savefig('commuting_modes_by_semester_plot.png', dpi=300, bbox_inches='tight')
plt.show()

