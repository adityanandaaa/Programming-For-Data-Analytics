# =====================================================================
# CONVERSION INTELLIGENCE: NEURAL NETWORK MODEL
# Objective: Predict e-commerce purchase intent (Revenue) using 
# 7 high-impact behavioral and contextual variables.
#
# Data Source: UCI Machine Learning Repository
# Link: https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset
# =====================================================================

# ---------------------------------------------------------------------
# 1. Data Loading & Cleaning
# ---------------------------------------------------------------------
# Load the dataset (ensure your working directory contains the CSV)
# Download from: https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset
df <- read.csv("online_shoppers_intention.csv") 

# Remove any rows containing missing values to prevent model errors
df <- na.omit(df)

# ---------------------------------------------------------------------
# 2. Feature Engineering & Preprocessing
# ---------------------------------------------------------------------
# Target Variable: Convert boolean (TRUE/FALSE) to binary (1/0)
df$Revenue <- ifelse(df$Revenue == TRUE, 1, 0)

# Categorical Variable: Convert 'VisitorType' to binary 
# (1 = Returning Visitor, 0 = New/Other Visitor)
df$Visitor_Returning <- ifelse(df$VisitorType == "Returning_Visitor", 1, 0)

# Continuous Variables: Apply Z-score normalization (scaling)
# This ensures variables with large ranges (like Duration) do not 
# overpower variables with small ranges (like Rates).
df$Administrative          <- scale(df$Administrative)
df$ProductRelated_Duration <- scale(df$ProductRelated_Duration)
df$BounceRates             <- scale(df$BounceRates)
df$ExitRates               <- scale(df$ExitRates)
df$PageValues              <- scale(df$PageValues)
df$SpecialDay              <- scale(df$SpecialDay)

# ---------------------------------------------------------------------
# 3. Train / Test Data Split (70/30)
# ---------------------------------------------------------------------
# Dynamically calculate the 70% split index based on the dataset size
split_index <- floor(nrow(df) * 0.70)

# Split the data into training and evaluation sets
df_train <- df[1:split_index, ]
df_test  <- df[(split_index + 1):nrow(df), ]

# ---------------------------------------------------------------------
# 4. Neural Network Training
# ---------------------------------------------------------------------
library(neuralnet)

# Train the ANN using the 7 strategic business variables
nn <- neuralnet(Revenue ~ Administrative + ExitRates + PageValues + 
                          ProductRelated_Duration + BounceRates + 
                          Visitor_Returning + SpecialDay,
                data          = df_train,
                hidden        = 5,           # 1 hidden layer with 5 nodes
                act.fct       = "logistic",  # Logistic activation for binary outcome
                linear.output = FALSE)       # Output probabilities, not continuous numbers

# Visualize the network architecture
plot(nn)

# ---------------------------------------------------------------------
# 5. Model Evaluation & Business Metrics
# ---------------------------------------------------------------------
# Generate predictions on the unseen test dataset
predicted <- compute(nn, df_test[, c("Administrative", "ExitRates", "PageValues", 
                                     "ProductRelated_Duration", "BounceRates", 
                                     "Visitor_Returning", "SpecialDay")])

# Apply the strategic 0.3 probability threshold to maximize buyer recall
predicted_Revenue <- ifelse(predicted$net.result > 0.3, 1, 0)
actual_Revenue    <- df_test$Revenue 

# Build and display the Confusion Matrix
cm <- table(Predicted = predicted_Revenue, Actual = actual_Revenue)
cat("\n--- CONFUSION MATRIX ---\n")
print(cm)

# Extract quadrants for strategic metric calculations [Row, Column]
true_negative  <- cm[1, 1] 
false_negative <- cm[1, 2] 
false_positive <- cm[2, 1] 
true_positive  <- cm[2, 2] 

# Calculate the core business metrics
accuracy  <- (true_positive + true_negative) / sum(cm)
precision <- true_positive / (true_positive + false_positive)
recall    <- true_positive / (true_positive + false_negative)

# Output the strategic metrics cleanly
cat("\n--- STRATEGIC METRICS ---\n")
cat("Overall Accuracy : ", round(accuracy * 100, 2), "%\n", sep="")
cat("Precision        : ", round(precision * 100, 2), "% (Quality of buyer alerts)\n", sep="")
cat("Recall           : ", round(recall * 100, 2), "% (Percentage of actual buyers caught)\n", sep="")
cat("-------------------------\n")

# ---------------------------------------------------------------------
# 6. Predictor Evaluation (Variable Importance)
# ---------------------------------------------------------------------
library(NeuralNetTools)

# Calculate variable importance using Olden's algorithm
imp <- olden(nn, bar_plot = FALSE)

cat("\n--- VARIABLE IMPORTANCE RANKING ---\n")
print(imp[order(imp$importance, decreasing = TRUE), , drop = FALSE])

# Visualize the operational hooks
olden(nn)