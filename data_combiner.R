# Script to read in all of the google analytics queries

# Deal with the weird format and headers
queary_reader <- function(data_file){
    read.delim(data_file ,sep="\t", header=TRUE,
              fileEncoding="UTF-16", skip = 15)
    }

# Get all query files
file_list <- list.files("data")[grep("query", list.files("data"))]

# Loop though reading all files and combining them
for (x in file_list){
    file_path <- paste0("data/", x)
    query_data <- queary_reader(file_path)
    if (exists("all_data")) {
        all_data <- rbind(all_data, query_data)
    }else{
        all_data <- query_data
    }
        
}

# Write out to csv
write.csv(all_data, "data/all_queries.csv", row.names = FALSE)