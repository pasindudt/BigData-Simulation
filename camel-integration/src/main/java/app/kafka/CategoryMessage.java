package app.kafka;

import java.time.Instant;

public class CategoryMessage {
   private String action;
   private String entity;
   private CategoryData data;

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

   public CategoryData getData() {
      return data;
   }

   public void setData(CategoryData data) {
      this.data = data;
   }

   public static class CategoryData {
      private String category_id;
      private String name;
      private Instant created_at;
      private Instant updated_at;
      private Instant deleted_at;

      public String getCategory_id() {
         return category_id;
      }

      public void setCategory_id(String category_id) {
         this.category_id = category_id;
      }

      public String getName() {
         return name;
      }

      public void setName(String name) {
         this.name = name;
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
