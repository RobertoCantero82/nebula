###############################################################################
# Analysis code for:
# "A Large-Scale Analysis of Temporal Patterns in Children's Purported
#  Past-Life Memories: Shorter Intervals Following Unexpected Deaths"
#
# Reproduces all results reported in the manuscript from the
# data file CORT_IT_open_data.csv (see CORT_IT_codebook.txt for variable
# definitions).
#
# R version 4.5.1. 
###############################################################################

library(dplyr)
library(moments)

## ---------------------------------------------------------------------------
## Helper: Pearson correlation with 95% CI, t, df, and p
## ---------------------------------------------------------------------------
report_cor <- function(x, y, method = "pearson") {
  ct <- if (method == "pearson") cor.test(x, y, method = "pearson")
  else cor.test(x, y, method = method, exact = FALSE)
  n <- sum(complete.cases(x, y))
  if (method == "pearson") {
    cat(sprintf("r(%d) = %.3f, 95%% CI [%.3f, %.3f], t = %.2f, p = %s, N = %d\n",
                ct$parameter, ct$estimate, ct$conf.int[1], ct$conf.int[2],
                ct$statistic, format.pval(ct$p.value, digits = 3), n))
  } else {
    cat(sprintf("Spearman r = %.3f, p = %s, N = %d\n",
                ct$estimate, format.pval(ct$p.value, digits = 3), n))
  }
  invisible(ct)
}

## ---------------------------------------------------------------------------
## Load data
## ---------------------------------------------------------------------------
data_file<- "CORT_IT_open_data.csv"
dat <- read.csv(data_file, na.strings = "")

# All analyses use verified cases (previous person identified)
dat <- dat %>% filter(is_verified)

# Log-transform intermission time.
# Note: the minimum observed intermission time is -3 months (cases in which
# the recorded birth precedes the recorded death date); a constant of +4 is
# added before the log10 transformation so it is defined for all cases.
dat$intermp_log <- log10(dat$intermp + 4)

###############################################################################
# TABLE 1: Number of available data for each study variable
###############################################################################
cat("\n=== TABLE 1: Available N per variable (verified cases) ===\n")
cat("Verified cases:            ", nrow(dat), "\n")
cat("Intermission time:         ", sum(!is.na(dat$intermp)), "\n")
cat("Death unexpectedness:      ", sum(!is.na(dat$death_unexp)), "\n")
cat("Naturalness of death:      ", sum(!is.na(dat$NATURAL_DEATH)), "\n")
cat("Age at death:              ", sum(!is.na(dat$agedhp)), "\n")
cat("Verification precision:    ", sum(!is.na(dat$stringent_verif)), "\n")
cat("Memory contamination:      ", sum(!is.na(dat$no_or_wrong_memory)), "\n")
cat("Family association:        ", sum(!is.na(dat$family_assoc)), "\n")
cat("Social status difference:  ", sum(!is.na(dat$social_status_diff_recoded)), "\n")
cat("Reincarnation belief:      ", sum(!is.na(dat$believeReinc_S)), "\n")

###############################################################################
# DESCRIPTIVE STATISTICS (Figure 1)
###############################################################################
cat("\n=== Descriptive statistics ===\n")

## Naturalness of death (Figure 1A)
counts_nat <- table(dat$NATURAL_DEATH)
cat(sprintf("Unnatural deaths: %.0f%% (n = %d)\n",
            100 * counts_nat["0"] / sum(counts_nat), counts_nat["0"]))
cat(sprintf("Natural deaths:   %.0f%% (n = %d)\n",
            100 * counts_nat["1"] / sum(counts_nat), counts_nat["1"]))

## Unexpectedness (Figure 1B)
counts_unexp <- table(dat$death_unexp)
cat(sprintf("Completely unexpected (rating 4): %.0f%%\n",
            100 * counts_unexp["4"] / sum(counts_unexp)))

## Inter-correlations among death characteristics (Figure 1D)
cat("\nNaturalness x Unexpectedness (chi-square):\n")
print(chisq.test(table(dat$NATURAL_DEATH, dat$death_unexp)))

cat("Naturalness x Age at death (Wilcoxon):\n")
print(wilcox.test(agedhp ~ NATURAL_DEATH, data = dat))
median_ages <- tapply(dat$agedhp, dat$NATURAL_DEATH, median, na.rm = TRUE) / 12
cat(sprintf("Median age: unnatural = %.0f years, natural = %.0f years\n",
            median_ages["0"], median_ages["1"]))

cat("Unexpectedness x Age at death (Pearson):\n")
report_cor(dat$death_unexp, dat$agedhp)

## Intermission time distribution (Figure 1E)
x <- dat$intermp[!is.na(dat$intermp)]
cat(sprintf("\nIT skewness = %.2f\n", skewness(x)))
print(agostino.test(x, alternative = "two.sided"))
cat(sprintf("Median IT: %.0f months (IQR: %.0f-%.0f)\n",
            median(x), quantile(x, .25), quantile(x, .75)))
cat(sprintf("Maximum IT: %.0f years\n", max(x) / 12))

###############################################################################
# PRIMARY HYPOTHESIS TESTING (Table 2, Figure 2)
###############################################################################
cat("\n=== TABLE 2: Correlations with log(IT) ===\n")

cat("Unexpectedness x log(IT):\n");  report_cor(dat$death_unexp,   dat$intermp_log)
cat("Naturalness x log(IT):\n");     report_cor(dat$NATURAL_DEATH, dat$intermp_log)
cat("Age at death x log(IT):\n");    report_cor(dat$agedhp,        dat$intermp_log)

## Spearman sensitivity check
cat("\nSpearman sensitivity check:\n")
cat("Unexpectedness: "); report_cor(dat$death_unexp,   dat$intermp_log, "spearman")
cat("Naturalness:    "); report_cor(dat$NATURAL_DEATH, dat$intermp_log, "spearman")
cat("Age at death:   "); report_cor(dat$agedhp,        dat$intermp_log, "spearman")

## Multiple regression: unexpectedness and naturalness as joint predictors
cat("\nMultiple regression (unexpectedness + naturalness):\n")
m_primary <- lm(intermp_log ~ death_unexp + NATURAL_DEATH, data = dat)
print(summary(m_primary))

## Median IT by unexpectedness rating (Figure 2)
cat("\nMedian IT by unexpectedness rating:\n")
med_by_unexp <- dat %>%
  filter(!is.na(death_unexp) & !is.na(intermp)) %>%
  group_by(death_unexp) %>%
  summarise(median_IT = median(intermp), n = n())
print(med_by_unexp)

expected_IT   <- median(dat$intermp[dat$death_unexp < 4],  na.rm = TRUE)
unexpected_IT <- median(dat$intermp[dat$death_unexp == 4], na.rm = TRUE)
cat(sprintf("Some anticipation (0-3): %.0f months; completely unexpected (4): %.0f months (%.0f%% shorter)\n",
            expected_IT, unexpected_IT,
            100 * (expected_IT - unexpected_IT) / expected_IT))

natural_IT   <- median(dat$intermp[dat$NATURAL_DEATH == 1], na.rm = TRUE)
unnatural_IT <- median(dat$intermp[dat$NATURAL_DEATH == 0], na.rm = TRUE)
cat(sprintf("Natural deaths: %.0f months; unnatural deaths: %.0f months (%.0f%% shorter)\n",
            natural_IT, unnatural_IT,
            100 * (natural_IT - unnatural_IT) / natural_IT))

###############################################################################
# MODERATION ANALYSES (Table 3, Figure 3)
###############################################################################

## --------------------------------------------------------------------------
## 1. Verification precision
## --------------------------------------------------------------------------
cat("\n=== Moderator 1: Verification precision ===\n")

cat("Stringently verified cases:\n")
with(subset(dat, stringent_verif),  report_cor(death_unexp, intermp_log))
cat("Non-stringently verified cases:\n")
with(subset(dat, !stringent_verif), report_cor(death_unexp, intermp_log))

cat("Interaction model:\n")
print(summary(lm(intermp_log ~ death_unexp * stringent_verif, data = dat)))

## --------------------------------------------------------------------------
## 2. Memory contamination
## --------------------------------------------------------------------------
cat("\n=== Moderator 2: Memory contamination ===\n")

cat("No or inaccurate memory of mode of death (no possible contamination):\n")
with(subset(dat, no_or_wrong_memory),  report_cor(death_unexp, intermp_log))
cat("Accurate memory of mode of death (possible contamination):\n")
with(subset(dat, !no_or_wrong_memory), report_cor(death_unexp, intermp_log))

cat("Interaction model:\n")
print(summary(lm(intermp_log ~ death_unexp * no_or_wrong_memory, data = dat)))

## --------------------------------------------------------------------------
## 3. Family association
## --------------------------------------------------------------------------
cat("\n=== Moderator 3: Family association ===\n")

cat("Distribution of family association levels:\n")
print(round(100 * prop.table(table(dat$family_assoc)), 0))

cat("Main-effect model (controlling for family association):\n")
print(summary(lm(intermp_log ~ death_unexp + family_assoc, data = dat)))

cat("Interaction model:\n")
print(summary(lm(intermp_log ~ death_unexp * family_assoc, data = dat)))

## --------------------------------------------------------------------------
## 4. Social status
## --------------------------------------------------------------------------
cat("\n=== Moderator 4: Social status ===\n")

status_sign <- sign(dat$social_status_diff_recoded)
pp_higher <- sum(status_sign ==  1, na.rm = TRUE)
pp_same   <- sum(status_sign ==  0, na.rm = TRUE)
pp_lower  <- sum(status_sign == -1, na.rm = TRUE)
cat(sprintf("PP higher status: %d; same: %d; PP lower status: %d\n",
            pp_higher, pp_same, pp_lower))

cat("Binomial test (higher vs. lower, H0: p = .5):\n")
print(binom.test(pp_higher, pp_higher + pp_lower, p = 0.5))

cat("Main-effect model (controlling for social status difference):\n")
print(summary(lm(intermp_log ~ death_unexp + social_status_diff_recoded, data = dat)))

cat("Interaction model:\n")
print(summary(lm(intermp_log ~ death_unexp * social_status_diff_recoded, data = dat)))

## --------------------------------------------------------------------------
## 5. Belief in reincarnation
## --------------------------------------------------------------------------
cat("\n=== Moderator 5: Belief in reincarnation ===\n")

cat("Distribution of reincarnation-favorable religious affiliation:\n")
print(round(100 * prop.table(table(dat$believeReinc_S)), 0))

cat("Believing families:\n")
with(subset(dat, believeReinc_S == 1), report_cor(death_unexp, intermp_log))
cat("Non-believing families:\n")
with(subset(dat, believeReinc_S == 0), report_cor(death_unexp, intermp_log))

cat("Interaction model:\n")
print(summary(lm(intermp_log ~ death_unexp * believeReinc_S, data = dat)))
