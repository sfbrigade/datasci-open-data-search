

queary_reader <- function(data_file){
    read.delim(data_file ,sep="\t", header=TRUE,
              fileEncoding="UTF-16", skip = 15)
    }

file_list <- list.files("data")[grep("query", list.files("data"))]

for (x in file_list){
    file_path <- paste0("data/", x)
    query_data <- queary_reader(file_path)
    if (exists("all_data")) {
        all_data <- rbind(all_data, query_data)
    }else{
        all_data <- query_data
    }
        
}


write.csv(all_data, "data/all_queries.csv", row.names = FALSE)