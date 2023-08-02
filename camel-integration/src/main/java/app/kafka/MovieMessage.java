package app.kafka;

import java.time.Instant;

public class MovieMessage {
   private String action;
   private String entity;
   private MovieData data;

   public String getAction() {
      return action;
   }

   public void setAction(String action) {
      this.action = action;
   }

   public String getEntity() {
      return entity;
   }

   public void setEntity(String entity) {
      this.entity = entity;
   }

   public MovieData getData() {
      return data;
   }

   public void setData(MovieData data) {
      this.data = data;
   }

   public static class MovieData {
      private String movie_id;
      private String title;
      private String release_date;
      private String category;
      private Instant created_at;
      private Instant updated_at;
      private Instant deleted_at;

      public String getMovie_id() {
         return movie_id;
      }

      public void setMovie_id(String movie_id) {
         this.movie_id = movie_id;
      }

      public String getTitle() {
         return title;
      }

      public void setTitle(String title) {
         this.title = title;
      }

      public String getRelease_date() {
         return release_date;
      }

      public void setRelease_date(String release_date) {
         this.release_date = release_date;
      }

      public String getCategory() {
         return category;
      }

      public void setCategory(String category) {
         this.category = category;
      }

      public Instant getCreated_at() {
         return created_at;
      }

      public void setCreated_at(Instant created_at) {
         this.created_at = created_at;
      }

      public Instant getUpdated_at() {
         return updated_at;
      }

      public void setUpdated_at(Instant updated_at) {
         this.updated_at = updated_at;
      }

      public Instant getDeleted_at() {
         return deleted_at;
      }

      public void setDeleted_at(Instant deleted_at) {
         this.deleted_at = deleted_at;
      }
   }
}
