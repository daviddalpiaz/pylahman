#!/usr/bin/env Rscript
# Extract column names from the Lahman R package and output as JSON

# force reinstall to ensure we have the latest version
install.packages("Lahman", repos = "https://cloud.r-project.org", quiet = TRUE)

library(Lahman)
library(jsonlite)

# get all data objects in the Lahman package
tables <- c(
  "AllstarFull",
  "Appearances",
  "AwardsManagers",
  "AwardsPlayers",
  "AwardsShareManagers",
  "AwardsSharePlayers",
  "Batting",
  "BattingPost",
  "CollegePlaying",
  "Fielding",
  "FieldingOF",
  "FieldingOFsplit",
  "FieldingPost",
  "HallOfFame",
  "HomeGames",
  "Managers",
  "ManagersHalf",
  "Parks",
  "People",
  "Pitching",
  "PitchingPost",
  "Salaries",
  "Schools",
  "SeriesPost",
  "Teams",
  "TeamsFranchises",
  "TeamsHalf"
)

# extract column names for each table
result <- list()
for (table_name in tables) {
  df <- get(table_name)
  result[[table_name]] <- names(df)
}

# output as JSON to same directory as this script
args <- commandArgs(trailingOnly = FALSE)
script_path <- sub("--file=", "", args[grep("--file=", args)])
if (length(script_path) == 0) {
  # fallback if run interactively
  script_path <- "scripts/extract-r-columns.R"
}
output_path <- file.path(dirname(script_path), "r-package-columns.json")
write_json(result, output_path, pretty = TRUE, auto_unbox = TRUE)
cat("Wrote", output_path, "\n")
